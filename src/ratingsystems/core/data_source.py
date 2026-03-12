import cbbd
import json
import os
from abc import ABC, abstractmethod
from dataclasses import asdict
from datetime import datetime
from typing import Type

from ratingsystems.core.model import Game, GameStats, Stat
from ratingsystems.core.util import config_path


class DataSource(ABC):

    class Meta:
        name: str = ""
        stats_class: Type = Stat

    def __init__(self, year: int = datetime.now().year, include_incomplete: bool = False):
        self.year = year

    def cli(self, context):
        games = self.fetch()
        self.save(games)

    @abstractmethod
    def fetch(self) -> list[Game]:
        raise NotImplementedError()

    @property
    def data_dir(self) -> str:
        import ratingsystems
        data_dir = os.path.join(config_path, "data")
        if not os.path.exists(data_dir):
            os.mkdir(data_dir)
        return data_dir

    @property
    def data_path(self) -> str:
        return os.path.join(self.data_dir, f"{self.Meta.name}-{self.year}.json")

    @property
    def auth_token(self) -> str:
        auth_path = os.path.join(config_path, "auth", f"{self.Meta.name}")
        if not os.path.exists(auth_path):
            return None
        else:
            with open(auth_path, "r") as f:
                auth_token = f.read()
            return auth_token

    @auth_token.setter
    def auth_token(self, value: str):
        auth_path = os.path.join(config_path, "auth", f"{self.Meta.name}")
        if not os.path.exists(os.path.dirname(auth_path)):
            os.mkdir(os.path.dirname(auth_path))
        with open(auth_path, "w") as f:
            f.write(value)


    def save(self, games: list[Game]):
        with open(self.data_path, "w") as f:
            json.dump([asdict(game) for game in games], f, default=str)

    def load(self, incomplete: bool = True) -> list[Game]:
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"No data found on local device for {self.Meta.name} {self.year}")

        with open(self.data_path, "r") as f:
            if hasattr(self.Meta, "stats_class"):
                games = [Game(**game, stats_class=self.Meta.stats_class) for game in json.load(f)]
            else:
                games = [Game(**game) for game in json.load(f)]
        if not incomplete:
            return [game for game in games if game.complete]
        return games

    def __str__(self) -> str:
        return self.Meta.name

    def __repr__(self) -> str:
        return self.Meta.name
