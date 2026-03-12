from typing import Optional


class Prediction():

    def __init__(self, team: str, opponent: str, line: Optional[float] = None, odds: Optional[float] = None, team_score: Optional[float] = None, opponent_score: Optional[float] = None):
        self.team = team
        self.opponent = opponent
        self.line = line
        self.odds = odds
        self.team_score = team_score
        self.opponent_score = opponent_score

    def __str__(self) -> str:
        if self.team_score is not None and self.opponent_score is not None:
            return f"{self.team} ({self.odds}) [{self.team_score}] vs [{self.opponent_score}] {self.opponent} ({1 - self.odds}) [{self.line}]"
        return f"{self.team} ({self.odds}) vs {self.opponent} ({1 - self.odds}) [{self.line}]"

    def __repr__(self) -> str:
        return str(self)