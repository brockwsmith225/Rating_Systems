from abc import ABC, abstractmethod
from inspect import signature

import click
from click.core import ParameterSource

from ratingsystems.core.model import Game, Rating


class RatingSystem(ABC):
    """
    Abstract class used to create a rating system.

    Classes that inherit from RatingSystem must implement a rate method which takes as input a list of Game objects and returns a Rating object.
    
    Classes that inherit from RatingSystem must also implement a #Meta class. See Meta class below for more details.

    Classes that inherit from RatingSystem can accept any options to __init__, but they must have a default value.
    """

    class Meta:
        """
        Meta class for a rating system. Any class that inherits from RatingSystem must override this Meta class and set the name field.
        """
        name: str = ""

    def __init__(self):
        pass

    @abstractmethod
    def rate(self, games: list[Game]) -> Rating:
        """
        Method to create a rating based on game data.

        Args:
            games (list[#Game]): list of games

        Returns:
            #Rating object with a rating for each team found in the game data
        """
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.Meta.name

    def __repr__(self) -> str:
        return self.Meta.name
