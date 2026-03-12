import scipy.stats as st
from abc import abstractmethod
from inspect import signature
from typing import Optional

import click
from click.core import ParameterSource

from ratingsystems.core.model import Prediction, Rating


class Predictor():

    class Meta:
        name: str = ""

    def __init__(self, rating: Rating):
        self.rating = rating

    @abstractmethod
    def predict(self, team: str, opponent: str) -> Prediction:
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.Meta.name

    def __repr__(self) -> str:
        return self.Meta.name


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

    def predict(self, team: str, opponent: str) -> Prediction:
        line = (self.rating.get_value(team) - self.rating.get_value(opponent))
        return Prediction(
            team,
            opponent,
            line=line,
            odds=float(st.norm.cdf(line / self.rating.confidence_interval)),
        )
