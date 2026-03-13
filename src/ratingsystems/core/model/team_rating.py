from collections.abc import Iterable
from typing import Optional, Self

from ratingsystems.core.model.stat import Stat


class TeamRating():
    """
    Class representing a team and its ratings. This includes any sub ratings of the #Rating that produced this #TeamRating.

    Parameters:
    - `name` _str_ - name of the team
    - `rating` _Stat_ - rating of the team, represented by a #Stat object
    - `wins` _int_ - number of games the team has won
    - `losses` _int_ - number of games the team has lost
    - `ties` _int_ - number of games the team has tied
    - `**sub_rating` - additional #TeamRating objects to be stored as sub ratings for the #TeamRating; can be accessed via a property based on the name of the #Rating that produced the #TeamRating
    """

    def __init__(self, name: str, rating: Stat, wins: int = 0, losses: int = 0, ties: int = 0, **sub_ratings):
        self.name = name
        self.rating = rating
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self._sub_ratings = sub_ratings
        for k, v in sub_ratings.items():
            setattr(self, k, v)

    def ratings(self, hidden: bool = False) -> Iterable[Stat]:
        """
        Iterator for the ratings, which gives a #Rating object for this team's rating and all sub ratings.

        Args:
            hidden (bool): include hidden ratings, i.e. ones whose name begins with an underscore ('_')
        """
        return iter([self.rating] + [rating for name, r in self._sub_ratings.items() for rating in r.ratings(hidden=hidden) if hidden or not name.startswith("_")])

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"<{self.name}={self.rating.value}>"
