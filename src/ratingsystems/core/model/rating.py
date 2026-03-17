import math
from abc import ABC, abstractmethod
from collections.abc import Iterable
from functools import cached_property
from numbers import Number
from statistics import stdev
from typing import Any, Optional, Self, Type, Union

from ratingsystems.core.model.team_rating import TeamRating
from ratingsystems.core.model.game import Game
from ratingsystems.core.model.stat import Stat


class Rating():
    """
    Class representing a rating of teams. This class also provides many helpful functions for interacting with the ratings.

    Parameters:
    - `rating` _dict[str, #Stat]_ - mapping of team names to ratings, ratings should be represented by a #Stat object
    - `games` _list[#Game]_ - list of games used to generate this rating
    - `name` _str_ - name of the rating; when transforming #Rating objects through arithmetic operators, #Rating objects with names will be accessible in the resulting #Rating object via a property based on the name; names that begin with an underscore ('_') will be hidden and will not appear unless explicitly requested (default: None)
    - `stat_class` _Type[#Stat]_ - #Stat type that, if specified, is used to convert ratings (default: None)
    - `reverse_sort` _bool_ - whether to reverse the order when sorting the #Rating (default: False)
    - `**auxillary_data` - additional fields to be stored on the #Rating; this can be sub rating, additional data needed for a predictor, or anything else useful to a consumer of the rating
    
    #Rating objects are iterable. Iterating on a #Rating object will yield a #TeamRating representing each team.

    All of the arithmetic operators work on #Rating objects just like regular numbers. The result of these arithmetic operators will be a new #Rating object that contains the original ratings transformed by the arithmetic operation.<br>
    ```(rating + 1).get_value(team) == rating.get_value(team) + 1```<br>
    ```(2 * rating).get_value(team) == 2 * rating.get_value(team)```<br>
    ```(rating1 - rating2).get_value(team) == rating1.get_value(team) - rating2.get_value(team)```

    This can be used to create new ratings that are combinations of existing ratings. For example, it may be useful in a rating system to create simple ratings, then combine and transform these into more complex ratings, without having to do so across all teams. It may also be useful to modify and/or combine ratings from different rating systems.

    #Rating objects with a name will be accessible in the resulting #Rating object via a property based on the name of the #Rating object.<br>
    ```named_rating = Rating(data, games, name="abc")```<br>
    ```(named_rating + 1).abc == named_rating```
    
    The following useful operations can also be achieved using other operators.

    You can add or change the name of a #Rating object using the modulo operator ('%')<br>
    ```rating = (rating1 + rating2) % "new_name"```<br>
    This can be especially useful when combined with the arithmetic operators to give names to the new ratings you're creating.

    You can add a #Rating object as a sub rating of another #Rating object using the left shift operator ('<<')<br>
    ```rating = (rating1 + rating2) << sub_rating```<br>
    This can be useful to add additional ratings that weren't used in calculating your rating. (Note: the sub rating must have a name, otherwise this operation will fail) 

    You can cast the ratings of a #Rating object to a different #Stat class using the or operator ('|')<br>
    ```> rating = (rating1 + rating2) | Stat```<br>
    This can be useful when you are combining two ratings with one #Stat type, but wish for the resulting rating to be a different #Stat type.

    You can reverse the sort order of a #Rating object using the invert operator ('~')<br>
    ```> reversed_rating = ~(rating1 + rating2)```<br>
    This can be useful when you are combining two ratings, but wish for the resulting rating to have the reverse sort order.
    """

    def __init__(self, rating: Union[dict[str, Stat], Any], games: list[Game], name: str = None, stat_class: Type[Stat] = None, reverse_sort: bool = False, **auxilliary_data):
        if isinstance(rating, dict):
            for team, value in rating.items():
                if not issubclass(type(value), Stat):
                    rating[team] = Stat(value)

        self.name = name
        self._rating = rating
        self.games = games

        self._stat_class = stat_class
        self._reverse_sort = reverse_sort

        self._sub_ratings = {}

        if isinstance(self._rating, _Combination):
            if isinstance(self._rating._first_rating, Rating):
                if self._rating._first_rating.name is not None and self._rating._first_rating.name != self.name:
                    self._sub_ratings[self._rating._first_rating.name] = self._rating._first_rating
                    setattr(self, self._rating._first_rating.name, self._rating._first_rating)
                else:
                    for name, rating in self._rating._first_rating._sub_ratings.items():
                        self._sub_ratings[name] = rating
                        setattr(self, name, rating)
            if isinstance(self._rating._second_rating, Rating):
                if self._rating._second_rating.name is not None and self._rating._second_rating.name != self.name:
                    self._sub_ratings[self._rating._second_rating.name] = self._rating._second_rating
                    setattr(self, self._rating._second_rating.name, self._rating._second_rating)
                else:
                    for name, rating in self._rating._second_rating._sub_ratings.items():
                        self._sub_ratings[name] = rating
                        setattr(self, name, rating)

        for name, data in auxilliary_data.items():
            setattr(self, name, data)
            if isinstance(data, Rating):
                self._sub_ratings[name] = data

    def get(self, team: str) -> Optional[Stat]:
        """
        Get a rating for a team.

        Args:
            team (str): name of the team to get the rating for

        Returns:
            #Stat representing the rating of the team, if team exists
        """
        if self._stat_class:
            return self._stat_class(self._rating.get(team).value)
        return self._rating.get(team)

    def get_value(self, team: str) -> Optional[Number]:
        """
        Get a rating value for a team.

        Args:
            team (str): name of the team to get the rating for

        Returns:
            float representation of the rating of the team, if team exists
        """
        if self._rating.get(team) is None:
            return None
        return self._rating.get(team).value

    def get_zscore(self, team: str) -> Optional[Number]:
        """
        Get the Z-score of a rating for a team.

        Args:
            team (str): team name to get the Z-score for

        Returns:
            Number representation of the Z-score of the rating of the team, if team exists
        """
        if self.get_value(team) is None:
            return None
        if self.stdev == 0:
            return 0
        return (self.get_value(team) - self.mean) / self.stdev

    def get_team(self, team: str) -> Optional[TeamRating]:
        """
        Get a team and all of their ratings.

        Args:
            team (str): name of the team to get

        Returns:
            #TeamRating representation of the team and all their ratings, if team exists
        """
        if self.get(team) is None:
            return None
        return TeamRating(
            name=team,
            rating=self.get(team),
            wins=len([1 for game in self.games if (game.home_team == team and game.home_winner) or (game.away_team == team and game.away_winner)]) if self.games else 0,
            losses=len([1 for game in self.games if (game.home_team == team and game.away_winner) or (game.away_team == team and game.home_winner)]) if self.games else 0,
            conference=[game.home_conference if game.home_team == team else game.away_conference for game in self.games if game.home_team == team or game.away_team == team][0],
            **{name: rating.get_team(team) for name, rating in self._sub_ratings.items()},
        )

    def get_rank(self, team: str) -> int:
        """
        Get the rank of a team by rating.

        Args:
            team (str): name of the team to get the rank of

        Returns:
            integer ranking of the team
        """
        return self.ranking.get(team)

    @cached_property
    def confidence_interval(self) -> float:
        """
        Property reprenting the confidence interval of the rating. Calculated as the standard deviation of the difference between the rating difference and the margin of victory for each game. Useful for creating odds from a predicted line or a line from predicted odds.
        """
        if not self.games:
            return None
        return stdev([(self.get_value(game.home_team) - self.get_value(game.away_team)) - (game.home_points - game.away_points) for game in self.games])

    @cached_property
    def mean(self) -> float:
        """
        Property reprenting the mean of the rating.
        """
        if self._mean is not None:
            return self._mean
        ratings_values = [team.rating.value for team in self]
        return sum(ratings_values) / len(ratings_values)

    @cached_property
    def stdev(self) -> float:
        """
        Property reprenting the standard deviation of the rating.
        """
        ratings_values = [team.rating.value for team in self]
        return math.sqrt(sum([pow(v - self.mean, 2) for v in ratings_values]) / len(ratings_values))

    @cached_property
    def ranking(self) -> dict[str, int]:
        """
        Property reprenting rankings of all teams in the rating.
        """
        ranking = sorted(list(iter(self)), key=lambda t: t.rating.value)
        if not self._reverse_sort:
            ranking = list(reversed(ranking))
        return {team.name: r + 1 for r, team in enumerate(ranking)}

    def __iter__(self) -> Iterable[TeamRating]:
        team_ratings = []
        for team in self._rating.keys():
            team_ratings.append(self.get_team(team))
        return iter(team_ratings)

    def keys(self) -> Iterable[str]:
        """
        Iterator for the rating keys, which corresponds to the team names.
        """
        return self._rating.keys()

    def values(self) -> Iterable[str]:
        """
        Iterator for the rating values, which corresponds to the ratings.
        """
        return self._rating.values()

    def teams(self) -> Iterable[str]:
        """
        Iterator for the teams included in the rating.
        """
        return self.keys()

    def ratings(self, hidden: bool = False) -> Iterable[Self]:
        """
        Iterator for the ratings, which gives a #Rating object for this object and each sub rating, recursively.

        Args:
            hidden (bool): include hidden ratings, i.e. ones whose name begins with an underscore ('_')
        """
        if self.name is not None:
            return iter([self] + [rating for r in self._sub_ratings.values() for rating in r.ratings(hidden=hidden) if hidden or not r.name.startswith("_")])
        else:
            return iter([rating for r in self._sub_ratings.values() for rating in r.ratings(hidden=hidden) if hidden or not r.name.startswith("_")])

    @staticmethod
    def rank(rating: Self) -> list[TeamRating]:
        """
        Rank teams by rating.

        Args:
            rating (#Rating): rating to use for the ranking
            reverse (bool): whether to reverse the rankings

        Returns:
            list of teams represented as a #TeamRating, in order by each team's rating
        """

        ranking = sorted(list(iter(rating)), key=lambda t: t.rating.value)
        if not rating._reverse_sort:
            return list(reversed(ranking))
        return [rating.get_team(team) for team in self.ranking.keys()]

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
            return Rating(self._rating, name=other, games=self.games, stat_class=self._stat_class, reverse_sort=self._reverse_sort, **sub_ratings)
        else:
            raise TypeError(f"Unsupported operand type(s) for %: 'Rating' and '{type(other)}'")

    def __lshift__(self, other: Any) -> Self:
        """
        Create a Rating with an additional Rating added to its sub ratings.
        """
        if isinstance(other, Rating):
            if other.name is not None:
                return Rating(self._rating, name=self.name, games=self.games, stat_class=self._stat_class, reverse_sort=self._reverse_sort, **self._sub_ratings, **{other.name: other})
            else:
                raise TypeError("Cannot add sub rating without a name")
        else:
            raise TypeError(f"Unsupported operand type(s) for <<: 'Rating' and '{type(other)}'")

    def __or__(self, other: Any) -> Self:
        """
        Create a Rating where its ratings are cast to a Stat class.
        """
        if issubclass(other, Stat):
            return Rating(self._rating, name=self.name, games=self.games, stat_class=other, reverse_sort=self._reverse_sort, **self._sub_ratings)
        else:
            raise TypeError(f"Unsupported operand type(s) for |: 'Rating' and '{type(other)}'")

    def __invert__(self) -> Self:
        """
        Create a Rating with reverse_sort made opposite.
        """
        return Rating(self._rating, name=self.name, games=self.games, stat_class=self._stat_class, reverse_sort=not self._reverse_sort, **self._sub_ratings)

    def __repr__(self) -> str:
        if self.name:
            return f"Rating<{self.name}>"
        else:
            return "Rating<>"


class _Combination(ABC):

    def __init__(self, first_rating: Rating, second_rating: Union[Rating, Number] = None):
        if isinstance(first_rating, Rating):
            self._first_rating = first_rating
        else:
            self._first_rating = {t: first_rating for t in second_rating.keys()}
        if isinstance(second_rating, Rating):
            self._second_rating = second_rating
        else:
            self._second_rating = {t: second_rating for t in first_rating.keys()}

        self._rating = {t: self._get(t) for t in self.keys()}

    def keys(self):
        return self._first_rating.keys() | self._second_rating.keys()

    def values(self) -> list[Stat]:
        return self._rating.values()

    def get(self, team: str) -> Stat:
        return self._rating.get(team)

    @abstractmethod
    def _get(self, team: str) -> Stat:
        raise NotImplementedError()


class _Add(_Combination):

    def _get(self, team: str) -> Optional[Stat]:
        if self._first_rating.get(team) is None or self._second_rating.get(team) is None:
            return None
        return self._first_rating.get(team) + self._second_rating.get(team)


class _Subtract(_Combination):

    def _get(self, team: str) -> Optional[Stat]:
        if self._first_rating.get(team) is None or self._second_rating.get(team) is None:
            return None
        return self._first_rating.get(team) - self._second_rating.get(team)


class _Multiply(_Combination):

    def _get(self, team: str) -> Optional[Stat]:
        if self._first_rating.get(team) is None or self._second_rating.get(team) is None:
            return None
        return self._first_rating.get(team) * self._second_rating.get(team)


class _Divide(_Combination):

    def _get(self, team: str) -> Stat:
        if self._first_rating.get(team) is None or self._second_rating.get(team) is None:
            return None
        return self._first_rating.get(team) / self._second_rating.get(team)


class _Pow(_Combination):

    def _get(self, team: str) -> Optional[Stat]:
        if self._first_rating.get(team) is None or self._second_rating.get(team) is None:
            return None
        return self._first_rating.get(team) ** self._second_rating.get(team)


class _AbsoluteValue(_Combination):

    def _get(self, team: str) -> Optional[Stat]:
        if self._first_rating.get(team) is None:
            return None
        return abs(self._first_rating.get(team))
