from collections.abc import Iterable
from typing import Optional, Self

from ratingsystems.core.model.stat import Stat


class TeamRating():

    def __init__(self, name: str, rating: Stat, wins: int = 0, losses: int = 0, ties: int = 0, **sub_ratings):
        self.name = name
        self.rating = rating
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self._sub_ratings = sub_ratings
        for k, v in sub_ratings.items():
            setattr(self, k, v)

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"<{self.name}={self.rating.value}>"

    def ratings(self, hidden: bool = False) -> Iterable[Stat]:
        return iter([self.rating] + [rating for name, r in self._sub_ratings.items() for rating in r.ratings(hidden=hidden) if hidden or not name.startswith("_")])

    @staticmethod
    def combine(*ratings, rating: Optional[Stat] = None, **sub_ratings):
        if rating is None and ratings:
            rating = ratings[0].rating
        combined_team = None
        for team in ratings:
            if combined_team is None:
                combined_team = TeamRating(
                    name=team.name,
                    rating=rating,
                    wins=team.wins,
                    losses=team.losses,
                    ties=team.ties,
                    **team._extra_ratings,
                )
            else:
                combined_team = TeamRating(
                    name=combined_team.name,
                    rating=rating,
                    wins=combined_team.wins,
                    losses=combined_team.losses,
                    ties=combined_team.ties,
                    **{k: v for k, v in team._extra_ratings if k not in combined_team._extra_ratings},
                    **combined_team._extra_ratings,
                )
        for sub_rating, team in sub_ratings.items():
            if combined_team is None:
                combined_team = TeamRating(
                    name=team.name,
                    rating=rating,
                    wins=team.wins,
                    losses=team.losses,
                    ties=team.ties,
                    **{sub_rating: team},
                )
            else:
                combined_team = TeamRating(
                    name=combined_team.name,
                    rating=rating,
                    wins=combined_team.wins,
                    losses=combined_team.losses,
                    ties=combined_team.ties,
                    **{sub_rating: team} if sub_rating not in combined_team._extra_ratings else {},
                    **combined_team._extra_ratings,
                )
        return combined_team

