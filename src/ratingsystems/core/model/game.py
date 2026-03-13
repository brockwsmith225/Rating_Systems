from dataclasses import dataclass, field, InitVar
from datetime import datetime
from typing import Any, Optional, Type


@dataclass
class GameStats():
    """
    Class that represents stats for a team in a game.

    Can be inheritted by another class to add more stats.

        points: int
        period_points: list[int]
    """
    points: int = field()
    period_points: list[int] = field()


@dataclass
class Game():
    """
    Class that represents a game.

        id: int
        season: int
        home_team: str
        away_team: str
        preseason: bool
        postseason: bool
        start_date: Optional[datetime]
        neutral_site: bool
        conference_game: bool
        complete: bool
        overtime: bool
        home_conference: Optional[str]
        home_seed: Optional[int]
        home_points: Optional[int]
        home_period_points: list[int]
        home_winner: Optional[bool]
        home_stats: Optional[GameStats]
        away_conference: Optional[str]
        away_seed: Optional[int]
        away_points: Optional[int]
        away_period_points: list[int]
        away_winner: Optional[bool]
        away_stats: Optional[GameStats]
        stats_class: InitVar[Optional[Type[GameStats]]]
    """
    id: int = field()
    season: int = field()
    home_team: str = field()
    away_team: str = field()
    preseason: bool = field(default=False)
    postseason: bool = field(default=False)
    start_date: Optional[datetime] = field(default=None)
    neutral_site: bool = field(default=False)
    conference_game: bool = field(default=False)
    complete: bool = field(default=True)
    overtime: bool = field(default=False)
    home_conference: Optional[str] = field(default=None)
    home_seed: Optional[int] = field(default=None)
    home_points: Optional[int] = field(default=None)
    home_period_points: list[int] = field(default_factory=list)
    home_winner: Optional[bool] = field(default=None)
    home_stats: Optional[GameStats] = field(default=None)
    away_conference: Optional[str] = field(default=None)
    away_seed: Optional[int] = field(default=None)
    away_points: Optional[int] = field(default=None)
    away_period_points: list[int] = field(default_factory=list)
    away_winner: Optional[bool] = field(default=None)
    away_stats: Optional[GameStats] = field(default=None)
    stats_class: InitVar[Optional[Type[GameStats]]] = field(default=None)

    def __post_init__(self, stats_class):
        if self.complete:
            self.home_winner = self.home_points > self.away_points
            self.away_winner = self.away_points > self.home_points

        if stats_class is not None:
            self.home_stats = stats_class(**self.home_stats)
            self.away_stats = stats_class(**self.away_stats)
