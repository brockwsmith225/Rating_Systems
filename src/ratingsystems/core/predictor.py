"""
Defines a predictor, which can be used to predict a matchup between two teams.

A predictor can be used by calling the #predict function with a team and an opponent. This will return a #Prediction of the matchup.

This is also exposed via the CLI command `predict`, which can be called like this:
```bash
ratingsystems predict TEAM OPPONENT --data <datasource> --rating <ratingsystem> --predictor <predictor>
```
"""
import scipy.stats as st
from abc import ABC, abstractmethod
from inspect import signature
from typing import Optional

import click
from click.core import ParameterSource

from ratingsystems.core.model import Prediction, Rating


class Predictor(ABC):
    """
    Abstract class used to create a predictor.

    Classes that inherit from #Predictor must implement a #predict method which takes as input a team and an opponent and returns a #Prediction object.

    Classes that inherit from #Predictor can accept any options to __init__, but they must have a default value, and it must accept a #Rating as its first argument.
    
    Classes that inherit from #Predictor should override the name class attribute to give their predictor a name.
    """

    name: str = ""
    "_str_ Name of predictor; will be used by the CLI, so ideally this is short"

    def __init__(self, rating: Rating):
        self.rating = rating

    @abstractmethod
    def predict(self, team: str, opponent: str) -> Prediction:
        """
        Method to predict a matchup of two teams.

        Args:
            team (str): first team of the matchup
            opponent (str): second team of the matchup

        Returns:
            #Prediction object with prediction for the matchup
        """
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class AggregatePredictor():

    def __init__(self, *predictors: list[Predictor], weights: Optional[list[float]] = None):
        self.predictors = predictors

        if not weights:
            weights = [1 for _ in range(len(self.predictors))]
        self.weights = weights

    def predict(self, team: str, opponent: str) -> Prediction:
        predictions = [predictor.predict(team, opponent) for predictor in self.predictors]
        return Prediction(
            team,
            opponent,
            line=self._average([prediction.line for prediction in predictions if prediction.line is not None]),
            odds=self._average([prediction.odds for prediction in predictions if prediction.odds is not None]),
            team_score=self._average([prediction.team_score for prediction in predictions if prediction.team_score is not None]),
            opponent_score=self._average([prediction.opponent_score for prediction in predictions if prediction.opponent_score is not None]),
        )

    def _average(self, values: list[float]) -> float:
        return sum([values[i] * self.weights[i] for i in range(len(values))]) / sum(self.weights)


class RatingDifferencePredictor(Predictor):

    name: str = "diff"

    def predict(self, team: str, opponent: str) -> Prediction:
        line = (self.rating.get_value(team) - self.rating.get_value(opponent))
        return Prediction(
            team,
            opponent,
            line=line,
            odds=float(st.norm.cdf(line / self.rating.confidence_interval)),
        )
