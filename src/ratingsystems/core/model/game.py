from dataclasses import dataclass, field, InitVar
from datetime import datetime
from typing import Any, Optional, Type


@dataclass
class GameStats():
    points: int = field()
    period_points: list[int] = field()


@dataclass
class Game():
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
    overtime: bool = field(default=True)
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
