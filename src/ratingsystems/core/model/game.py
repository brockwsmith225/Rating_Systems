from dataclasses import dataclass, field, InitVar
from datetime import datetime
from typing import Any, Optional, Type


@dataclass
class GameStats():
    """
    Class representing stats for a team in a game.

    Can be inheritted by another class to add more stats.
    """

    points: Optional[int] = field()
    "(int) Points scored"

    period_points: list[int] = field()
    "(list[int]) Points scored in each period"


@dataclass
class Game():
    """
    Class representing a game.
    """

    id: int = field()
    "(int) Unique id for this game"

    season: int = field()
    "(int) Season this game was played in"

    home_team: str = field()
    "(str) Name of the home team"

    away_team: str = field()
    "(str) Name of the away team"

    preseason: bool = field(default=False)
    "(bool) Whether this game was in the preseason (default: False)"

    postseason: bool = field(default=False)
    "(bool) Whether this game was in the postseason (default: False)"

    start_date: Optional[datetime] = field(default=None)
    "(datetime) Start date of the game (default: None)"

    neutral_site: bool = field(default=False)
    "(bool) Whether this game was played at a neutral site (default: False)"

    conference_game: bool = field(default=False)
    "(bool) Whether this game was a conference game (default: False)"

    complete: bool = field(default=True)
    "(bool) Whether this game is complete (default: True)"

    overtime: bool = field(default=False)
    "(bool) Whether this game went to overtime (default: False)"

    home_conference: Optional[str] = field(default=None)
    "(str) Name of the conference of the home team (default: None)"

    home_seed: Optional[int] = field(default=None)
    "(int) Seed of the home team (default: None)"

    home_points: Optional[int] = field(default=None)
    "(int) Points scored by the home team (default: None)"

    home_period_points: list[int] = field(default_factory=list)
    "(list[int]) Points scored by the home team in each period (default: None)"

    home_winner: Optional[bool] = field(default=None)
    "(bool) Whether the home team won (default: None)"

    home_stats: Optional[GameStats] = field(default=None)
    "(#GameStats) Additional stats for the home team (default: None)"

    away_conference: Optional[str] = field(default=None)
    "(str) Name of the conference of the away team (default: None)"

    away_seed: Optional[int] = field(default=None)
    "(int) Seed of the away team (default: None)"

    away_points: Optional[int] = field(default=None)
    "(int) Points scored by the away team (default: None)"

    away_period_points: list[int] = field(default_factory=list)
    "(list[int]) Points scored by the away team in each period (default: None)"

    away_winner: Optional[bool] = field(default=None)
    "(bool) Whether the away team won (default: None)"

    away_stats: Optional[GameStats] = field(default=None)
    "(#GameStats) Additional stats for the away team (default: None)"

    stats_class: InitVar[Optional[Type[GameStats]]] = field(default=None)
    "(type[#GameStats]) Class to use for the game stats; useful if you want to include additional stats for a game (default: #GameStats)"

    def __post_init__(self, stats_class):
        if self.complete:
            self.home_winner = self.home_points > self.away_points
            self.away_winner = self.away_points > self.home_points

        if stats_class is not None:
            if self.home_stats is not None:
                self.home_stats = stats_class(**self.home_stats)
            if self.away_stats is not None:
                self.away_stats = stats_class(**self.away_stats)
