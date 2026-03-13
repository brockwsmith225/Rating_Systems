from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Prediction():
    """
    Class representing a prediction.
    """

    team: str = field()
    "(str) Name of the team"

    opponent: str = field()
    "(str) Name of the opponent"

    line: Optional[float] = field(default=None)
    "(float) Predicted line of the matchup (default: None)"

    odds: Optional[float] = field(default=None)
    "(float) Predicted odds of the matchup (default: None)"

    team_score: Optional[float] = field(default=None)
    "(float) Predicted score of team in the matchup (default: None)"

    opponent_score: Optional[float] = field(default=None)
    "(float) Predicted score of opponent in the matchup (default: None)"

    # TODO: auto create line/odds ? this would need the rating passed to the prediction
    # def __post_init__(self):
    #     if self.line is None and self.team_score is not None and self.opponent_score is not None:
    #         pass
    #     if self.rating is not None:
    #         if self.odds is None and self.line is not None:
    #             pass
    #         if self.line is None and self.odds is not None:
    #             pass

    def __str__(self) -> str:
        if self.team_score is not None and self.opponent_score is not None:
            return f"{self.team} ({self.odds}) [{self.team_score}] vs [{self.opponent_score}] {self.opponent} ({1 - self.odds}) [{self.line}]"
        return f"{self.team} ({self.odds}) vs {self.opponent} ({1 - self.odds}) [{self.line}]"

    def __repr__(self) -> str:
        return str(self)