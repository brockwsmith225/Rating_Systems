from abc import abstractmethod
from inspect import signature

import click
from click.core import ParameterSource

from ratingsystems.core.model import Game, Rating


class RatingSystem():

    class Meta:
        name: str = ""

    def __init__(self):
        pass

    @abstractmethod
    def rate(self, games: list[Game]) -> Rating:
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.Meta.name

    def __repr__(self) -> str:
        return self.Meta.name
