"""
Defines a rating system, which can be used to create a rating of teams.

A rating system can be used by calling the #rate function with a list of #Game. This will return a #Rating of the teams.

This is also exposed via the CLI command `rate`, which can be called like this:
```bash
ratingsystems rate --data <datasource> --rating <ratingsystem>
```
"""
from abc import ABC, abstractmethod
from inspect import signature

import click
from click.core import ParameterSource

from ratingsystems.core.model import Game, Rating


class RatingSystem(ABC):
    """
    Abstract class used to create a rating system.

    Classes that inherit from #RatingSystem must implement a #rate method which takes as input a list of #Game objects and returns a #Rating object.

    Classes that inherit from #RatingSystem can accept any options to __init__, but they must have a default value.
    
    Classes that inherit from #RatingSystem should override the name class attribute to give their rating system a name.
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
        return self.name

    def __repr__(self) -> str:
        return self.name
