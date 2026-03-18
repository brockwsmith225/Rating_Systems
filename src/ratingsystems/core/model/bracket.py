from dataclasses import dataclass, field
from typing import Callable, Optional, Self, Union

from ratingsystems.core.predictor import Predictor


@dataclass
class Bracket:
    """
    Class representing a bracket. This class also provides the #Bracket.evaluate method to evaluate the odds of the bracket using a #Predictor.
    """

    subbracket_1: Optional[Union[str, Self]]
    "(str or #Bracket) One side of the bracket up to this point; a string value should be a team name"

    subbracket_2: Optional[Union[str, Self]]
    "(str or #Bracket) The other side of the bracket up to this point; a string value should be a team name"

    seed_1: Optional[int] = field(default=None)
    "(int) Seed of one side of the bracket; likely only exists when subbracket_1 is a team name (default: None)"

    seed_2: Optional[int] = field(default=None)
    "(int) Seed of the other side of the bracket; likely only exists when subbracket_2 is a team name (default: None)"

    bracket_name: str = field(default="")
    "(str) Display name of the bracket (default: '')"

    odds: dict[str, float] = field(default=None)
    "(dict[str, float]) Mapping of teams in the bracket to the odds they make it to this point in the bracket"

    results: dict[str, int] = field(default_factory=dict)
    "(dict[str, float]) Mapping of teams in the bracket to the round they lost in"

    @property
    def depth(self) -> int:
        """
        Property giving the depth of this point in the bracket.
        """
        depth = 0
        if self.subbracket_1 is not None:
            if isinstance(self.subbracket_1, str):
                depth = 1
            else:
                depth = 1 + self.subbracket_1.depth
        if self.subbracket_2 is not None:
            if isinstance(self.subbracket_2, str):
                depth = max(1, depth)
            else:
                depth = max(1 + self.subbracket_2.depth, depth)
        return depth

    @property
    def teams(self) -> list[str]:
        """
        Property giving a list of teams in the bracket.
        """
        teams = []
        if self.depth == 1:
            if self.subbracket_1 is not None:
                teams.append(self.subbracket_1)
            if self.subbracket_2 is not None:
                teams.append(self.subbracket_2)
        else:
            return self.subbracket_1.teams + self.subbracket_2.teams
        return teams

    def evaluate(self, predictor: Predictor, results: dict[str, int] = {}, weight_by_seed: bool = False):
        """
        Evaluates the bracket to determine the odds for each team to reach each round, using a #Predictor. These odds are then stored in this bracket.

        Args:
            predictor (#Predictor): used to predict each possible matchup in the bracket
        """
        if len(results) == 0:
            results = self.results
        self.odds = {}
        if self.depth == 1:
            if self.subbracket_2 is None:
                self.odds[self.subbracket_1] = 1.0
            else:
                if results.get(self.subbracket_1) == self.depth:
                    game_odds = 0.0
                elif results.get(self.subbracket_2) == self.depth:
                    game_odds = 1.0
                else:
                    game_odds = predictor.predict(self.subbracket_1, self.subbracket_2).odds
                if weight_by_seed and self.seed_1 is not None and self.seed_2 is not None:
                    weight_1 = self.seed_1
                    weight_2 = self.seed_2
                    game_odds = game_odds * weight_1 / (game_odds * weight_1 + (1 - game_odds) * weight_2)
                self.odds[self.subbracket_1] = game_odds
                self.odds[self.subbracket_2] = 1.0 - game_odds
        else:
            self.subbracket_1.evaluate(predictor, results, weight_by_seed=weight_by_seed)
            self.subbracket_2.evaluate(predictor, results, weight_by_seed=weight_by_seed)
            for team_1 in self.subbracket_1.teams:
                self.odds[team_1] = 0.0
                for team_2 in self.subbracket_2.teams:
                    if not team_2 in self.odds:
                        self.odds[team_2] = 0.0
                    if results.get(team_1) == self.depth:
                        game_odds = 0.0
                    elif results.get(team_2) == self.depth:
                        game_odds = 1.0
                    else:
                        game_odds = predictor.predict(team_1, team_2).odds
                    if weight_by_seed:
                        seed_1 = self.get_seed(team_1)
                        seed_2 = self.get_seed(team_2)
                        if seed_1 is not None and seed_2 is not None:
                            weight_1 = seed_1
                            weight_2 = seed_2
                            game_odds = game_odds * weight_1 / (game_odds * weight_1 + (1 - game_odds) * weight_2)
                    self.odds[team_1] += game_odds * self.subbracket_1.odds[team_1] * self.subbracket_2.odds[team_2]
                    self.odds[team_2] += (1.0 - game_odds) * self.subbracket_1.odds[team_1] * self.subbracket_2.odds[team_2]

    @property
    def predicted_team(self) -> Optional[str]:
        """
        Property giving the team with the best odds to reach this point in the bracket. Will always return None until #Bracket.evaluate is run.
        """
        if not self.odds:
            return
        k = list(self.odds.keys())
        v = list(self.odds.values())
        return k[v.index(max(v))]

    @property
    def full_odds(self) -> Optional[dict[str, tuple[str, int, list[float]]]]:
        """
        Property giving the full odds to this point in the bracket. Will always return None until #Bracket.evaluate is run.

        This is formatted as a mapping from team names to a tuple containing in order the bracket name the team appears in, the team's seed, a list of odds for the team to reach each round.
        """
        if not self.odds:
            return
        if self.subbracket_2 is None:
            return {self.subbracket_1: (self.bracket_name, self.seed_1, [self.odds.get(self.subbracket_1)])}
        elif isinstance(self.subbracket_1, str):
            return {
                self.subbracket_1: (self.bracket_name, self.seed_1, [self.odds.get(self.subbracket_1)]),
                self.subbracket_2: (self.bracket_name, self.seed_2, [self.odds.get(self.subbracket_2)]),
            }

        subbracket_1_full_odds = self.subbracket_1.full_odds
        subbracket_2_full_odds = self.subbracket_2.full_odds
        full_odds = {**subbracket_1_full_odds, **subbracket_2_full_odds}
        for t, o in self.odds.items():
            full_odds[t][2].append(o)
        return full_odds

    def get_seed(self, team) -> Optional[int]:
        if team in self.subbracket_1:
            if self.seed_1 is not None:
                return self.seed_1
            return self.subbracket_1.get_seed(team)
        if team in self.subbracket_2:
            if self.seed_2 is not None:
                return self.seed_2
            return self.subbracket_2.get_seed(team)
        return None

    def __contains__(self, team) -> bool:
        if isinstance(self.subbracket_1, Bracket):
            if team in self.subbracket_1.teams:
                return True
        elif team == self.subbracket_1:
            return True
        if isinstance(self.subbracket_2, Bracket):
            if team in self.subbracket_2.teams:
                return True
        elif team == self.subbracket_2:
            return True
        return False

    def __str__(self) -> str:
        if self.depth == 1:
            if self.subbracket_2 is None:
                return f"{''.ljust(21)}\n{''.ljust(21)}\n{''.ljust(21)}"
            return f"{str(self.seed_1).rjust(2, ' ')} {self.subbracket_1.ljust(17, '-')}|\n{''.ljust(20)}|\n{str(self.seed_2).rjust(2, ' ')} {self.subbracket_2.ljust(17, '-')}|"
        else:
            subbracket_1_str = str(self.subbracket_1).split("\n")
            subbracket_2_str = str(self.subbracket_2).split("\n")

            middle = int(len(subbracket_1_str) / 2)

            for i in range(middle):
                subbracket_1_str[i] += f"{''.ljust(21)}"
            if self.subbracket_1.subbracket_2 is None:
                subbracket_1_str[middle] += f"{self.subbracket_1.subbracket_1.ljust(20, '-')}|"
            elif self.subbracket_1.predicted_team:
                subbracket_1_str[middle] += f"{self.subbracket_1.predicted_team.ljust(20, '-')}|"
            else:
                subbracket_1_str[middle] += f"{''.ljust(20, '-')}|"
            for i in range(middle + 1, len(subbracket_1_str)):
                subbracket_1_str[i] += f"{''.ljust(20)}|"

            for i in range(pow(2, self.depth - 1)):
                subbracket_1_str.append(f"{''.ljust(21 * self.depth - 1)}|")

            for i in range(middle):
                subbracket_2_str[i] += f"{''.ljust(20)}|"
            if self.subbracket_2.subbracket_2 is None:
                subbracket_2_str[middle] += f"{self.subbracket_2.subbracket_1.ljust(20, '-')}|"
            elif self.subbracket_2.predicted_team:
                subbracket_2_str[middle] += f"{self.subbracket_2.predicted_team.ljust(20, '-')}|"
            else:
                subbracket_2_str[middle] += f"{''.ljust(20, '-')}|"
            for i in range(middle + 1, len(subbracket_2_str)):
                subbracket_2_str[i] += f"{''.ljust(21)}"

            subbracket_1_str.extend(subbracket_2_str)
            return "\n".join(subbracket_1_str)

    def __repr__(self) -> str:
        return str(self)

    def to_file(self, path: str):
        """
        Saves this #Bracket object from to file.

        Args:
            path (str): path to the file to save the bracket to
        """
        raise NotImplementedError()

    @classmethod
    def from_file(cls, path: str) -> Self:
        """
        Loads a #Bracket from a file.

        Args:
            path (str): path to a file containing the bracket

        Returns:
            #Bracket object representing the bracket stored in the file
        """
        bracket = None
        current_brackets = []
        current_bracket_name = None
        results = {}
        with open(path, "r") as f:
            for line in f.readlines():
                # Bracket names are denoted by '--name'
                if line.startswith("--"):
                    current_bracket_name = line[2:].strip()
                    continue

                # Seeds are denoted by 'seed!team'
                if "!" in line:
                    seed = int(line.split("!")[0].strip())
                    team = line.split("!")[1].strip()
                else:
                    team = line

                # Play-in games are denoted by 'team1/team2'
                if "/" in team:
                    team1 = team.split("/")[0]
                    team2 = team.split("/")[1]
                    if "~" in team1:
                        result = int(team1.split("~")[1])
                        team1 = team1.split("~")[0]
                        results[team1] = result
                    if "~" in team2:
                        result = int(team2.split("~")[1])
                        team2 = team2.split("~")[0]
                        results[team2] = result
                    bracket = cls(team1, team2, seed, seed, current_bracket_name)
                else:
                    # Results are denoted by 'team~round' where round is the round the team lost in
                    if "~" in team:
                        result = int(team.split("~")[1])
                        team = team.split("~")[0]
                        results[team] = result
                    bracket = cls(team, None, seed, None, current_bracket_name)

                while len(current_brackets) > 0 and bracket.depth == current_brackets[-1].depth:
                    bracket = cls(current_brackets.pop(), bracket)

                current_brackets.append(bracket)

        bracket.results = results
        return bracket
