import functools
import math
import numpy as np
from abc import ABC, abstractmethod
from collections.abc import Iterable
from enum import Enum
from numbers import Number
from statistics import stdev
from typing import Any, Optional, Self, Union, Tuple, Type

from ratingsystems.core.model.prediction import Prediction
from ratingsystems.core.model.team_rating import TeamRating
from ratingsystems.core.model.game import Game
from ratingsystems.core.model.stat import Stat


class Rating():
    """
    Class representing a rating of teams. This class also provides many helpful functions for interacting with the ratings.

    Parameters:
        - rating (dict[str, #Stat]): mapping of team names to ratings, represented by a #Stat object
        - games (list[Game]): list of games used to generate this rating
        - name (str): name of the rating; when transforming #Rating objects through arithmetic operators, #Rating objects with names will be accessible in the resulting #Rating object via a property based on the name; names that begin with an underscore will be hidden and will not appear unless explicitly requested (default: None)
        - stat_class (Type[Stat]): Stat type that, if specified, is used to convert ratings (default: None)
        - **auxillary_data: additional fields to be stored on the #Rating; this can be sub rating, additional data needed for a predictor, or anything else useful to a consumer of the rating
    
    All of the arithmetic operators work on #Rating objects just like regular numbers. The result of these arithmetic operators will be a new #Rating object that contains the original ratings transformed by the arithmetic operation.
        ```python
        (rating + 1).get_value(team) == rating.get_value(team) + 1
        (2 * rating).get_value(team) == 2 * rating.get_value(team)
        (rating1 - rating2).get_value(team) == rating1.get_value(team) - rating2.get_value(team)
        ```

    This can be used to create new ratings that are combinations of existing ratings. For example, it may be useful in a rating system to create simple ratings, then combine and transform these into more complex ratings, without having to do so across all teams. It may also be useful to modify and/or combine ratings from different rating systems.

    #Rating objects with a name will be accessible in the resulting #Rating object via a property based on the name of the #Rating object.
        ```python
        named_rating = Rating(data, games, name="abc")
        (rating + 1).abc == named_rating
        ```
    
    The following useful operations can also be achieved using other operators.

    You can add or change the name of a #Rating object using the modulo operator (%)
        ```python
        rating = (rating1 + rating2) % "new_name"
        ```
    This can be especially useful when combined with the arithmetic operators to give names to the new ratings you're creating.

    You can add a #Rating object as a sub rating of another #Rating object using the left shift operator (<<)
        ```python
        rating = (rating1 + rating2) << sub_rating
        ```
    This can be useful to add additional ratings that weren't used in calculating your rating. (Note: the sub rating must have a name, otherwise this operation will fail) 

    You can cast the ratings of a #Rating object to a different #Stat class using the or operator (|)
        ```python
        rating = (rating1 + rating2) | #Stat
        ```
    This can be useful when you are combining two ratings with one #Stat type, but wish for the resulting rating to be a different #Stat type.
    """

    def __init__(self, rating: Union[dict[str, Stat], Any], games: list[Game], name: str = None, stat_class: Type[Stat] = None, **auxilliary_data):
        if isinstance(rating, dict):
            for team, value in rating.items():
                if not issubclass(type(value), Stat):
                    rating[team] = Stat(value)

        self.name = name
        self._rating = rating
        self.games = games

        self._stat_class = stat_class

        self._points = None
        self._confidence_interval = None
        self._mean = None
        self._stdev = None

        self._sub_ratings = {}

        if isinstance(self._rating, _Combination):
            if isinstance(self._rating.first_rating, Rating):
                if self._rating.first_rating.name is not None and self._rating.first_rating.name != self.name:
                    self._sub_ratings[self._rating.first_rating.name] = self._rating.first_rating
                    setattr(self, self._rating.first_rating.name, self._rating.first_rating)
                else:
                    for name, rating in self._rating.first_rating._sub_ratings.items():
                        self._sub_ratings[name] = rating
                        setattr(self, name, rating)
            if isinstance(self._rating.second_rating, Rating):
                if self._rating.second_rating.name is not None and self._rating.second_rating.name != self.name:
                    self._sub_ratings[self._rating.second_rating.name] = self._rating.second_rating
                    setattr(self, self._rating.second_rating.name, self._rating.second_rating)
                else:
                    for name, rating in self._rating.second_rating._sub_ratings.items():
                        self._sub_ratings[name] = rating
                        setattr(self, name, rating)

        for name, data in auxilliary_data.items():
            setattr(self, name, data)
            if isinstance(data, Rating):
                self._sub_ratings[name] = data

    def get(self, team: str) -> Stat:
        if self._stat_class:
            return self._stat_class(self._rating.get(team).value)
        return self._rating.get(team)

    def get_value(self, team: str) -> Number:
        return self.get(team).value

    def get_zscore(self, team: str) -> Number:
        return (self.get_value(team) - self.mean) / self.stdev

    def get_team(self, team: str) -> TeamRating:
        return TeamRating(
            name=team,
            rating=self.get(team),
            wins=len([1 for game in self.games if (game.home_team == team and game.home_winner) or (game.away_team == team and game.away_winner)]) if self.games else 0,
            losses=len([1 for game in self.games if (game.home_team == team and game.away_winner) or (game.away_team == team and game.home_winner)]) if self.games else 0,
            **{name: rating.get_team(team) for name, rating in self._sub_ratings.items()},
        )

    @property
    def confidence_interval(self) -> float:
        if self._confidence_interval is not None:
            return self._confidence_interval
        if not self.games:
            return None
        self._confidence_interval = stdev([(self.get_value(game.home_team) - self.get_value(game.away_team)) - (game.home_points - game.away_points) for game in self.games])
        return self._confidence_interval

    @property
    def mean(self) -> float:
        if self._mean is not None:
            return self._mean
        ratings_values = [team.rating.value for team in self]
        self._mean = sum(ratings_values) / len(ratings_values)
        return self._mean

    @property
    def stdev(self) -> float:
        if self._stdev is not None:
            return self._stdev
        ratings_values = [team.rating.value for team in self]
        self._stdev = math.sqrt(sum([pow(v - self.mean, 2) for v in ratings_values]) / len(ratings_values))
        return self._stdev

    def __iter__(self) -> Iterable[TeamRating]:
        team_ratings = []
        for team in self._rating.keys():
            team_ratings.append(self.get_team(team))
        return iter(team_ratings)

    def keys(self) -> Iterable[str]:
        return self._rating.keys()

    def teams(self) -> Iterable[str]:
        return self.keys()

    def ratings(self, hidden: bool = False) -> Iterable[Self]:
        return iter([self] + [rating for r in self._sub_ratings.values() for rating in r.ratings(hidden=hidden) if hidden or not r.name.startswith("_")])

    def __add__(self, other: Any) -> Self:
        if isinstance(other, Rating) or isinstance(other, Number):
            return Rating(_Add(self, other), games=self.games)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'Rating' and '{type(other)}'")

    def __radd__(self, other: Any) -> Self:
        if isinstance(other, Rating) or isinstance(other, Number):
            return Rating(_Add(other, self), games=self.games)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: '{type(other)}' and 'Rating'")

    def __sub__(self, other: Any) -> Self:
        if isinstance(other, Rating) or isinstance(other, Number):
            return Rating(_Subtract(self, other), games=self.games)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: 'Rating' and '{type(other)}'")

    def __rsub__(self, other: Any) -> Self:
        if isinstance(other, Rating) or isinstance(other, Number):
            return Rating(_Subtract(other, self), games=self.games)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: '{type(other)}' and 'Rating'")

    def __mul__(self, other: Any) -> Self:
        if isinstance(other, Rating) or isinstance(other, Number):
            return Rating(_Multiply(self, other), games=self.games)
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'Rating' and '{type(other)}'")

    def __rmul__(self, other: Any) -> Self:
        if isinstance(other, Rating) or isinstance(other, Number):
            return Rating(_Multiply(other, self), games=self.games)
        else:
            raise TypeError(f"Unsupported operand type(s) for *: '{type(other)}' and 'Rating'")

    def __truediv__(self, other: Any) -> Self:
        if isinstance(other, Rating) or isinstance(other, Number):
            return Rating(_Divide(self, other), games=self.games)
        else:
            raise TypeError(f"Unsupported operand type(s) for /: 'Rating' and '{type(other)}'")

    def __rtruediv__(self, other: Any) -> Self:
        if isinstance(other, Rating) or isinstance(other, Number):
            return Rating(_Divide(other, self), games=self.games)
        else:
            raise TypeError(f"Unsupported operand type(s) for /: '{type(other)}' and 'Rating'")

    def __pow__(self, other: Any) -> Self:
        if isinstance(other, Rating) or isinstance(other, Number):
            return Rating(_Pow(self, other), games=self.games)
        else:
            raise TypeError(f"Unsupported operand type(s) for **: 'Rating' and '{type(other)}'")

    def __rpow__(self, other: Any) -> Self:
        if isinstance(other, Rating) or isinstance(other, Number):
            return Rating(_Pow(other, self), games=self.games)
        else:
            raise TypeError(f"Unsupported operand type(s) for **: '{type(other)}' and 'Rating'")

    def __abs__(self) -> Self:
        return Rating(_AbsoluteValue(self), games=self.games)

    def __mod__(self, other: Any) -> Self:
        """
        Create a Rating with a new name.
        """
        if isinstance(other, str):
            sub_ratings = self._sub_ratings
            if other in sub_ratings:
                sub_ratings = {**sub_ratings[other]._sub_ratings, **sub_ratings}
                del sub_ratings[other]
            return Rating(self._rating, name=other, games=self.games, stat_class=self._stat_class, **sub_ratings)
        else:
            raise TypeError(f"Unsupported operand type(s) for %: 'Rating' and '{type(other)}'")

    def __lshift__(self, other: Any) -> Self:
        """
        Create a Rating with an additional Rating added to its sub ratings.
        """
        if isinstance(other, Rating):
            if other.name is not None:
                return Rating(self._rating, name=self.name, games=self.games, stat_class=self._stat_class, **self._sub_ratings, **{other.name: other})
            else:
                raise TypeError("Cannot add sub rating without a name")
        else:
            raise TypeError(f"Unsupported operand type(s) for <<: 'Rating' and '{type(other)}'")

    def __or__(self, other: Any) -> Self:
        """
        Create a Rating where its ratings are cast to a Stat class.
        """
        if issubclass(other, Stat):
            return Rating(self._rating, name=self.name, games=self.games, stat_class=other, **self._sub_ratings)
        else:
            raise TypeError(f"Unsupported operand type(s) for |: 'Rating' and '{type(other)}'")

    def __repr__(self) -> str:
        if self.name:
            return f"Rating<{self.name}>"
        else:
            return "Rating<>"

    @staticmethod
    def rank(rating: Self, reverse: bool = False) -> list[Tuple[str, Stat]]:
        ranking = sorted(list(iter(rating)), key=lambda t: -1 * t.rating.value)
        if reverse:
            return reversed(ranking)
        return ranking


class _Combination(ABC):

    def __init__(self, first_rating: Rating, second_rating: Union[Rating, Number] = None):
        if isinstance(first_rating, Rating):
            self.first_rating = first_rating
        else:
            self.first_rating = {t: first_rating for t in second_rating.keys()}
        if isinstance(second_rating, Rating):
            self.second_rating = second_rating
        else:
            self.second_rating = {t: second_rating for t in first_rating.keys()}

    def keys(self):
        return self.first_rating.keys() | self.second_rating.keys()

    @abstractmethod
    def get(self, team: str) -> Stat:
        raise NotImplementedError()


class _Add(_Combination):

    def get(self, team: str) -> Stat:
        return self.first_rating.get(team) + self.second_rating.get(team)


class _Subtract(_Combination):

    def get(self, team: str) -> Stat:
        return self.first_rating.get(team) - self.second_rating.get(team)


class _Multiply(_Combination):

    def get(self, team: str) -> Stat:
        return self.first_rating.get(team) * self.second_rating.get(team)


class _Divide(_Combination):

    def get(self, team: str) -> Stat:
        return self.first_rating.get(team) / self.second_rating.get(team)


class _Pow(_Combination):

    def get(self, team: str) -> Stat:
        return self.first_rating.get(team) ** self.second_rating.get(team)


class _AbsoluteValue(_Combination):

    def get(self, team: str) -> Stat:
        return abs(self.first_rating.get(team))


# class Rating():

#     def __init__(self, name: str, data: dict[str, TeamRating]):
#         self.name = name
#         if isinstance(data, StatReference):
#             self.teams = data.ratings.teams
#         else:
#             self.teams = data
#         for attribute in list(self.teams.values())[0].__dict__.keys():
#             if attribute == "name" or attribute.startswith("_"):
#                 continue
#             stat = StatReference(self, attribute)
#             setattr(self, attribute, stat)
#             self._stats = getattr(self, stat)

#     def get(self, team: str) -> TeamRating:
#         return self.teams[team]

#     def get_rating(self, team: str, default: float = None) -> Optional[float]:
#         if team not in self.teams:
#             return default
#         return self.teams[team].rating.value

#     def __iter__(self):
#         return self.teams.values()

#     # @staticmethod
#     # def from_expression(expression: Expression, stat: Type = Stat) -> Self:
#     #     return Rating({t.name: TeamRating(t.name, stat(expression.evaluate(t.name))) for t in expression.teams.values()})

#     @staticmethod
#     def rank(stat: Any, reverse: bool = False) -> list[TeamRating]:
#         if isinstance(stat, Rating):
#             stat = stat.rating
#         ranking = sorted(stat.ratings.teams.values(), key=lambda t: -1 * stat.get_value(t.name))
#         if reverse:
#             return reversed(ranking)
#         return ranking

#     @staticmethod
#     def normalize(rating: Self, minimum: Optional[float] = None) -> Self:
#         if minimum is None:
#             minimum = min([t.rating.value for t in rating])
#         total = sum([t.rating.value - minimum for t in rating])
#         print(minimum)
#         print(total)
#         return Rating(rating.name, {t.name: TeamRating(t.name, Stat((t.rating.value - minimum) / total)) for t in rating})

#     @staticmethod
#     def minmax_normalize(rating: Self, minimum: Optional[float] = None, maximum: Optional[float] = None) -> Self:
#         if minimum is None:
#             minimum = min([t.rating.value for t in rating.teams.values()])
#         if maximum is None:
#             maximum = max([t.rating.value for t in rating.teams.values()])
#         # total = sum([t.rating.value - minimum for t in rating.teams.values()])
#         print(minimum)
#         # print(total)
#         return Rating(rating.name, {t.name: TeamRating(t.name, Stat((t.rating.value - minimum) / (maximum - minimum))) for t in rating})

#     @staticmethod
#     def combine(first: Self, second: Self) -> Self:
#         return Rating({t.name: TeamRating(t.name, Stat(t.rating.value * second.get_rating(t.name))) for t in first})

#     def __repr__(self) -> str:
#         return f"Rating<{self.name}>"


# TODO: merge with Rating class so that each Rating represents a "primary rating"
# class StatReference():

#     def __init__(self, ratings: Rating, stat: str):
#         self.ratings = ratings
#         self.stat = stat
#         if isinstance(self.get(list(ratings.teams.keys())[0]), TeamRating):
#             for attribute in self.get(list(ratings.teams.keys())[0]).__dict__.keys():
#                 if attribute in ["name", "wins", "losses", "ties"] or attribute.startswith("_"):
#                     continue
#                 setattr(self, attribute, StatReference(ratings, f"{stat}.{attribute}"))

#     def get(self, team: str):
#         return functools.reduce(getattr, [self.ratings.get(team)] + self.stat.split('.'))

#     def get_value(self, team: str):
#         value = self.get(team)
#         return value.value if isinstance(value, Stat) else value

#     def __calculate(self, function, other):
#         new_teams = {}
#         if isinstance(other, StatReference):
#             for team in self.ratings.teams.keys() | other.ratings.teams.keys():
#                 self_value = self.get_value(team)
#                 other_value = other.get_value(team)
#                 new_teams[team] = TeamRating.combine(
#                     *[r.get(team) for r in [self.ratings, other.ratings] if r.name is None],
#                     **{r.name: r.get(team) for r in [self.ratings, other.ratings] if r.name is not None},
#                     rating=Stat(function(self_value, other_value)),
#                 )
#         elif other is not None:
#             for team in self.ratings.teams.keys():
#                 self_value = self.get_value(team)
#                 new_teams[team] = TeamRating.combine(
#                     *[r.get(team) for r in [self.ratings] if r.name is None],
#                     **{r.name: r.get(team) for r in [self.ratings] if r.name is not None},
#                     rating=Stat(function(self_value, other)),
#                 )
#         else:
#             for team in self.ratings.teams.keys():
#                 self_value = self.get_value(team)
#                 new_teams[team] = TeamRating.combine(
#                     *[r.get(team) for r in [self.ratings] if r.name is None],
#                     **{r.name: r.get(team) for r in [self.ratings] if r.name is not None},
#                     rating=Stat(function(self_value)),
#                 )

#         # Check that all the teams in all the ratings are in the combined rating
#         if new_teams.keys() - self.ratings.teams.keys():
#             raise ValueError(f"Teams '{list(new_teams.keys() - self.ratings.teams.keys())}' not found in all of '{other.ratings}'")
#         if isinstance(other, StatReference) and new_teams.keys() - other.ratings.teams.keys():
#             raise ValueError(f"Teams '{list(new_teams.keys() - other.ratings.teams.keys())}' not found in all of '{self.ratings}'")

#         return Rating(None, new_teams).rating

#     def __add__(self, other: Any) -> Self:
#         if isinstance(other, StatReference) or isinstance(other, Number):
#             return self.__calculate(lambda x, y: x + y, other)
#         else:
#             raise TypeError(f"Unsupported operand type(s) for +: 'StatReference' and '{type(other)}'")

#     def __sub__(self, other: Any) -> Rating:
#         if isinstance(other, StatReference) or isinstance(other, Number):
#             return self.__calculate(lambda x, y: x - y, other)
#         else:
#             raise TypeError(f"Unsupported operand type(s) for -: 'StatReference' and '{type(other)}'")

#     def __mul__(self, other: Any) -> Rating:
#         if isinstance(other, StatReference) or isinstance(other, Number):
#             return self.__calculate(lambda x, y: x * y, other)
#         else:
#             raise TypeError(f"Unsupported operand type(s) for *: 'StatReference' and '{type(other)}'")

#     def __truediv__(self, other: Any) -> Rating:
#         if isinstance(other, StatReference) or isinstance(other, Number):
#             return self.__calculate(lambda x, y: x / y, other)
#         else:
#             raise TypeError(f"Unsupported operand type(s) for /: 'StatReference' and '{type(other)}'")

#     def __abs__(self) -> Rating:
#         return self.__calculate(abs, None)

#     def __repr__(self) -> str:
#         return f"StatReference<{self.ratings}, {self.stat}>"
