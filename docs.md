# Table of Contents

* [ratingsystems](#ratingsystems)
* [ratingsystems.core.cli.cli](#ratingsystems.core.cli.cli)
  * [year](#ratingsystems.core.cli.cli.year)
  * [datasource](#ratingsystems.core.cli.cli.datasource)
  * [ratingsystem](#ratingsystems.core.cli.cli.ratingsystem)
  * [predictor](#ratingsystems.core.cli.cli.predictor)
  * [options](#ratingsystems.core.cli.cli.options)
  * [load\_cli\_plugins](#ratingsystems.core.cli.cli.load_cli_plugins)
  * [cli](#ratingsystems.core.cli.cli.cli)
  * [config](#ratingsystems.core.cli.cli.config)
  * [set\_defaults](#ratingsystems.core.cli.cli.set_defaults)
  * [fetch](#ratingsystems.core.cli.cli.fetch)
  * [rate](#ratingsystems.core.cli.cli.rate)
  * [predict](#ratingsystems.core.cli.cli.predict)
* [ratingsystems.core.cli.helpers](#ratingsystems.core.cli.helpers)
  * [combine\_key\_value\_pairs](#ratingsystems.core.cli.helpers.combine_key_value_pairs)
  * [filter\_options](#ratingsystems.core.cli.helpers.filter_options)
  * [SelectChoice](#ratingsystems.core.cli.helpers.SelectChoice)
    * [convert](#ratingsystems.core.cli.helpers.SelectChoice.convert)
  * [WeightedSelectChoice](#ratingsystems.core.cli.helpers.WeightedSelectChoice)
    * [convert](#ratingsystems.core.cli.helpers.WeightedSelectChoice.convert)
  * [KeyValuePair](#ratingsystems.core.cli.helpers.KeyValuePair)
    * [name](#ratingsystems.core.cli.helpers.KeyValuePair.name)
    * [convert](#ratingsystems.core.cli.helpers.KeyValuePair.convert)
    * [get\_metavar](#ratingsystems.core.cli.helpers.KeyValuePair.get_metavar)
* [ratingsystems.core.cli](#ratingsystems.core.cli)
* [ratingsystems.core.cli.\_\_main\_\_](#ratingsystems.core.cli.__main__)
  * [WIN\_WEIGHT](#ratingsystems.core.cli.__main__.WIN_WEIGHT)
  * [MAXIMUM\_MOV](#ratingsystems.core.cli.__main__.MAXIMUM_MOV)
  * [ALPHA](#ratingsystems.core.cli.__main__.ALPHA)
  * [MAXIMUM\_ITERATIONS](#ratingsystems.core.cli.__main__.MAXIMUM_ITERATIONS)
  * [cfb](#ratingsystems.core.cli.__main__.cfb)
  * [stats](#ratingsystems.core.cli.__main__.stats)
  * [predict](#ratingsystems.core.cli.__main__.predict)
  * [rrs](#ratingsystems.core.cli.__main__.rrs)
  * [rrs\_predict](#ratingsystems.core.cli.__main__.rrs_predict)
  * [rrs\_predict\_markov\_chain](#ratingsystems.core.cli.__main__.rrs_predict_markov_chain)
  * [ser](#ratingsystems.core.cli.__main__.ser)
  * [ser\_predict](#ratingsystems.core.cli.__main__.ser_predict)
  * [ser\_predict\_total](#ratingsystems.core.cli.__main__.ser_predict_total)
  * [zer](#ratingsystems.core.cli.__main__.zer)
  * [cer](#ratingsystems.core.cli.__main__.cer)
  * [cbb](#ratingsystems.core.cli.__main__.cbb)
  * [cbb\_stats](#ratingsystems.core.cli.__main__.cbb_stats)
  * [cbb\_bracket](#ratingsystems.core.cli.__main__.cbb_bracket)
  * [cbb\_test](#ratingsystems.core.cli.__main__.cbb_test)
* [ratingsystems.core.data\_source](#ratingsystems.core.data_source)
  * [DataSource](#ratingsystems.core.data_source.DataSource)
    * [name](#ratingsystems.core.data_source.DataSource.name)
    * [stats\_class](#ratingsystems.core.data_source.DataSource.stats_class)
    * [fetch](#ratingsystems.core.data_source.DataSource.fetch)
    * [save](#ratingsystems.core.data_source.DataSource.save)
    * [load](#ratingsystems.core.data_source.DataSource.load)
    * [data\_dir](#ratingsystems.core.data_source.DataSource.data_dir)
    * [data\_path](#ratingsystems.core.data_source.DataSource.data_path)
    * [auth\_token](#ratingsystems.core.data_source.DataSource.auth_token)
    * [auth\_token](#ratingsystems.core.data_source.DataSource.auth_token)
* [ratingsystems.core.model.bracket](#ratingsystems.core.model.bracket)
  * [Bracket](#ratingsystems.core.model.bracket.Bracket)
    * [subbracket\_1](#ratingsystems.core.model.bracket.Bracket.subbracket_1)
    * [subbracket\_2](#ratingsystems.core.model.bracket.Bracket.subbracket_2)
    * [seed\_1](#ratingsystems.core.model.bracket.Bracket.seed_1)
    * [seed\_2](#ratingsystems.core.model.bracket.Bracket.seed_2)
    * [bracket\_name](#ratingsystems.core.model.bracket.Bracket.bracket_name)
    * [odds](#ratingsystems.core.model.bracket.Bracket.odds)
    * [depth](#ratingsystems.core.model.bracket.Bracket.depth)
    * [teams](#ratingsystems.core.model.bracket.Bracket.teams)
    * [predicted\_team](#ratingsystems.core.model.bracket.Bracket.predicted_team)
    * [evaluate](#ratingsystems.core.model.bracket.Bracket.evaluate)
    * [full\_odds](#ratingsystems.core.model.bracket.Bracket.full_odds)
* [ratingsystems.core.model.game](#ratingsystems.core.model.game)
  * [GameStats](#ratingsystems.core.model.game.GameStats)
    * [points](#ratingsystems.core.model.game.GameStats.points)
    * [period\_points](#ratingsystems.core.model.game.GameStats.period_points)
  * [Game](#ratingsystems.core.model.game.Game)
    * [id](#ratingsystems.core.model.game.Game.id)
    * [season](#ratingsystems.core.model.game.Game.season)
    * [home\_team](#ratingsystems.core.model.game.Game.home_team)
    * [away\_team](#ratingsystems.core.model.game.Game.away_team)
    * [preseason](#ratingsystems.core.model.game.Game.preseason)
    * [postseason](#ratingsystems.core.model.game.Game.postseason)
    * [start\_date](#ratingsystems.core.model.game.Game.start_date)
    * [neutral\_site](#ratingsystems.core.model.game.Game.neutral_site)
    * [conference\_game](#ratingsystems.core.model.game.Game.conference_game)
    * [complete](#ratingsystems.core.model.game.Game.complete)
    * [overtime](#ratingsystems.core.model.game.Game.overtime)
    * [home\_conference](#ratingsystems.core.model.game.Game.home_conference)
    * [home\_seed](#ratingsystems.core.model.game.Game.home_seed)
    * [home\_points](#ratingsystems.core.model.game.Game.home_points)
    * [home\_period\_points](#ratingsystems.core.model.game.Game.home_period_points)
    * [home\_winner](#ratingsystems.core.model.game.Game.home_winner)
    * [home\_stats](#ratingsystems.core.model.game.Game.home_stats)
    * [away\_conference](#ratingsystems.core.model.game.Game.away_conference)
    * [away\_seed](#ratingsystems.core.model.game.Game.away_seed)
    * [away\_points](#ratingsystems.core.model.game.Game.away_points)
    * [away\_period\_points](#ratingsystems.core.model.game.Game.away_period_points)
    * [away\_winner](#ratingsystems.core.model.game.Game.away_winner)
    * [away\_stats](#ratingsystems.core.model.game.Game.away_stats)
    * [stats\_class](#ratingsystems.core.model.game.Game.stats_class)
* [ratingsystems.core.model.prediction](#ratingsystems.core.model.prediction)
  * [Prediction](#ratingsystems.core.model.prediction.Prediction)
    * [team](#ratingsystems.core.model.prediction.Prediction.team)
    * [opponent](#ratingsystems.core.model.prediction.Prediction.opponent)
    * [line](#ratingsystems.core.model.prediction.Prediction.line)
    * [odds](#ratingsystems.core.model.prediction.Prediction.odds)
    * [team\_score](#ratingsystems.core.model.prediction.Prediction.team_score)
    * [opponent\_score](#ratingsystems.core.model.prediction.Prediction.opponent_score)
* [ratingsystems.core.model.rating](#ratingsystems.core.model.rating)
  * [Rating](#ratingsystems.core.model.rating.Rating)
    * [get](#ratingsystems.core.model.rating.Rating.get)
    * [get\_value](#ratingsystems.core.model.rating.Rating.get_value)
    * [get\_zscore](#ratingsystems.core.model.rating.Rating.get_zscore)
    * [get\_team](#ratingsystems.core.model.rating.Rating.get_team)
    * [confidence\_interval](#ratingsystems.core.model.rating.Rating.confidence_interval)
    * [mean](#ratingsystems.core.model.rating.Rating.mean)
    * [stdev](#ratingsystems.core.model.rating.Rating.stdev)
    * [keys](#ratingsystems.core.model.rating.Rating.keys)
    * [teams](#ratingsystems.core.model.rating.Rating.teams)
    * [ratings](#ratingsystems.core.model.rating.Rating.ratings)
    * [rank](#ratingsystems.core.model.rating.Rating.rank)
* [ratingsystems.core.model.stat](#ratingsystems.core.model.stat)
  * [Stat](#ratingsystems.core.model.stat.Stat)
    * [formatted](#ratingsystems.core.model.stat.Stat.formatted)
* [ratingsystems.core.model.team\_rating](#ratingsystems.core.model.team_rating)
  * [TeamRating](#ratingsystems.core.model.team_rating.TeamRating)
    * [ratings](#ratingsystems.core.model.team_rating.TeamRating.ratings)
    * [combine](#ratingsystems.core.model.team_rating.TeamRating.combine)
* [ratingsystems.core.model](#ratingsystems.core.model)
* [ratingsystems.core.predictor](#ratingsystems.core.predictor)
  * [Predictor](#ratingsystems.core.predictor.Predictor)
    * [name](#ratingsystems.core.predictor.Predictor.name)
    * [predict](#ratingsystems.core.predictor.Predictor.predict)
  * [AggregatePredictor](#ratingsystems.core.predictor.AggregatePredictor)
    * [predict](#ratingsystems.core.predictor.AggregatePredictor.predict)
  * [RatingDifferencePredictor](#ratingsystems.core.predictor.RatingDifferencePredictor)
    * [name](#ratingsystems.core.predictor.RatingDifferencePredictor.name)
    * [predict](#ratingsystems.core.predictor.RatingDifferencePredictor.predict)
* [ratingsystems.core.rating\_system](#ratingsystems.core.rating_system)
  * [RatingSystem](#ratingsystems.core.rating_system.RatingSystem)
    * [name](#ratingsystems.core.rating_system.RatingSystem.name)
    * [rate](#ratingsystems.core.rating_system.RatingSystem.rate)
* [ratingsystems.core.util.file](#ratingsystems.core.util.file)
  * [config\_path](#ratingsystems.core.util.file.config_path)
* [ratingsystems.core.util.math](#ratingsystems.core.util.math)
  * [linear\_regression](#ratingsystems.core.util.math.linear_regression)
  * [logistic\_regression](#ratingsystems.core.util.math.logistic_regression)
  * [linear\_regression\_to\_points](#ratingsystems.core.util.math.linear_regression_to_points)
* [ratingsystems.core.util.text](#ratingsystems.core.util.text)
  * [center](#ratingsystems.core.util.text.center)
  * [ljustify](#ratingsystems.core.util.text.ljustify)
  * [rjustify](#ratingsystems.core.util.text.rjustify)
* [ratingsystems.core.util](#ratingsystems.core.util)
* [ratingsystems.core](#ratingsystems.core)

<a id="ratingsystems"></a>

# Module ratingsystems

<a id="ratingsystems.core.cli.cli"></a>

# Module ratingsystems.core.cli.cli

<a id="ratingsystems.core.cli.cli.year"></a>

## year

<a id="ratingsystems.core.cli.cli.datasource"></a>

## datasource

<a id="ratingsystems.core.cli.cli.ratingsystem"></a>

## ratingsystem

<a id="ratingsystems.core.cli.cli.predictor"></a>

## predictor

<a id="ratingsystems.core.cli.cli.options"></a>

## options

<a id="ratingsystems.core.cli.cli.load_cli_plugins"></a>

## load\_cli\_plugins

```python
def load_cli_plugins()
```

<a id="ratingsystems.core.cli.cli.cli"></a>

## cli

```python
@shell(prompt="ratingsystems > ",
       intro="Starting ratingsystems cli...",
       context_settings={'show_default': True})
@year
@datasource
@ratingsystem
@predictor
@options
@click.pass_context
def cli(context,
        year: int = datetime.now().year,
        datasource: Optional[DataSource] = None,
        ratingsystem: Optional[RatingSystem] = None,
        predictor: Optional[Predictor] = None,
        options: dict[str, Any] = {})
```

CLI for interacting with rating systems. Use without a subcommand to start a shell.

<a id="ratingsystems.core.cli.cli.config"></a>

## config

```python
@cli.command()
@year
@datasource
@ratingsystem
@predictor
@options
@click.pass_context
def config(context,
           year: int = datetime.now().year,
           datasource: Optional[DataSource] = None,
           ratingsystem: Optional[RatingSystem] = None,
           predictor: Optional[Predictor] = None,
           options: dict[str, Any] = {})
```

Used to set config values or see current config.

<a id="ratingsystems.core.cli.cli.set_defaults"></a>

## set\_defaults

```python
def set_defaults(
        context,
        new_parameters: Optional[dict[str, Any]] = None) -> dict[str, Any]
```

<a id="ratingsystems.core.cli.cli.fetch"></a>

## fetch

```python
@cli.command()
@year
@datasource
@click.pass_context
def fetch(context,
          year: int = datetime.now().year,
          datasource: Optional[DataSource] = None)
```

Used to fetch data.

<a id="ratingsystems.core.cli.cli.rate"></a>

## rate

```python
@cli.command()
@year
@datasource
@ratingsystem
@options
@click.option("--pretty/--no-pretty",
              type=bool,
              is_flag=True,
              default=False,
              help="Pretty print rating")
@click.option("--ranks/--no-ranks",
              type=bool,
              is_flag=True,
              default=False,
              help="Print ranks for each rating")
@click.option("--hidden/--no-hidden",
              type=bool,
              is_flag=True,
              default=False,
              help="Include hidden ratings in output")
@click.pass_context
def rate(context,
         year: int = datetime.now().year,
         datasource: Optional[DataSource] = None,
         ratingsystem: Optional[RatingSystem] = None,
         pretty: bool = False,
         ranks: bool = False,
         hidden: bool = False,
         options: dict[str, Any] = {})
```

Used to create a rating.

<a id="ratingsystems.core.cli.cli.predict"></a>

## predict

```python
@cli.group(invoke_without_command=True)
@click.argument("team", type=str)
@click.argument("opponent", type=str)
@year
@datasource
@ratingsystem
@predictor
@options
@click.pass_context
def predict(context,
            team: str,
            opponent: str,
            year: int = datetime.now().year,
            datasource: Optional[DataSource] = None,
            ratingsystem: Optional[RatingSystem] = None,
            predictor: Optional[Predictor] = None,
            options: dict[str, Any] = {})
```

Used to predict a matchup between TEAM and OPPONENT.


  TEAM first team in the matchup
  OPPONENT second team in the matchup

<a id="ratingsystems.core.cli.helpers"></a>

# Module ratingsystems.core.cli.helpers

<a id="ratingsystems.core.cli.helpers.combine_key_value_pairs"></a>

## combine\_key\_value\_pairs

```python
def combine_key_value_pairs(ctx: click.Context, param: click.Parameter,
                            value: tuple[dict[str, Any]]) -> dict[str, Any]
```

<a id="ratingsystems.core.cli.helpers.filter_options"></a>

## filter\_options

```python
def filter_options(options: dict[str, Any], cls: Type)
```

<a id="ratingsystems.core.cli.helpers.SelectChoice"></a>

## SelectChoice

```python
class SelectChoice(click.Choice)
```

<a id="ratingsystems.core.cli.helpers.SelectChoice.convert"></a>

### convert

```python
def convert(value: Optional[str] = None,
            param: Optional[click.Parameter] = None,
            ctx: Optional[click.Context] = None) -> Any
```

<a id="ratingsystems.core.cli.helpers.WeightedSelectChoice"></a>

## WeightedSelectChoice

```python
class WeightedSelectChoice(SelectChoice)
```

<a id="ratingsystems.core.cli.helpers.WeightedSelectChoice.convert"></a>

### convert

```python
def convert(value: Optional[str] = None,
            param: Optional[click.Parameter] = None,
            ctx: Optional[click.Context] = None) -> Any
```

<a id="ratingsystems.core.cli.helpers.KeyValuePair"></a>

## KeyValuePair

```python
class KeyValuePair(click.ParamType)
```

<a id="ratingsystems.core.cli.helpers.KeyValuePair.name"></a>

### name

<a id="ratingsystems.core.cli.helpers.KeyValuePair.convert"></a>

### convert

```python
def convert(value: Optional[str] = None,
            param: Optional[click.Parameter] = None,
            ctx: Optional[click.Context] = None) -> dict[str, Any]
```

<a id="ratingsystems.core.cli.helpers.KeyValuePair.get_metavar"></a>

### get\_metavar

```python
def get_metavar(param: click.Parameter,
                ctx: Optional[click.Context] = None) -> str
```

<a id="ratingsystems.core.cli"></a>

# Module ratingsystems.core.cli

<a id="ratingsystems.core.cli.__main__"></a>

# Module ratingsystems.core.cli.\_\_main\_\_

<a id="ratingsystems.core.cli.__main__.WIN_WEIGHT"></a>

## WIN\_WEIGHT

<a id="ratingsystems.core.cli.__main__.MAXIMUM_MOV"></a>

## MAXIMUM\_MOV

<a id="ratingsystems.core.cli.__main__.ALPHA"></a>

## ALPHA

<a id="ratingsystems.core.cli.__main__.MAXIMUM_ITERATIONS"></a>

## MAXIMUM\_ITERATIONS

<a id="ratingsystems.core.cli.__main__.cfb"></a>

## cfb

```python
def cfb(fetch_data=True)
```

<a id="ratingsystems.core.cli.__main__.stats"></a>

## stats

```python
def stats()
```

<a id="ratingsystems.core.cli.__main__.predict"></a>

## predict

```python
def predict(fetch_data: bool = True)
```

<a id="ratingsystems.core.cli.__main__.rrs"></a>

## rrs

```python
def rrs(games: list, win_weight: int = 30)
```

<a id="ratingsystems.core.cli.__main__.rrs_predict"></a>

## rrs\_predict

```python
def rrs_predict(rating: Rating, team: str, opponent: str)
```

<a id="ratingsystems.core.cli.__main__.rrs_predict_markov_chain"></a>

## rrs\_predict\_markov\_chain

```python
def rrs_predict_markov_chain(rating: Rating, team: str, opponent: str)
```

<a id="ratingsystems.core.cli.__main__.ser"></a>

## ser

```python
def ser(games: list, seed: Rating = None, k: float = 8.0)
```

<a id="ratingsystems.core.cli.__main__.ser_predict"></a>

## ser\_predict

```python
def ser_predict(rating: Rating, team: str, opponent: str)
```

<a id="ratingsystems.core.cli.__main__.ser_predict_total"></a>

## ser\_predict\_total

```python
def ser_predict_total(rating: Rating, team: str, opponent: str)
```

<a id="ratingsystems.core.cli.__main__.zer"></a>

## zer

```python
def zer(games: list, seed: Rating = None)
```

<a id="ratingsystems.core.cli.__main__.cer"></a>

## cer

```python
def cer(games: list, seed: Rating = None)
```

<a id="ratingsystems.core.cli.__main__.cbb"></a>

## cbb

```python
def cbb(fetch_data=True)
```

<a id="ratingsystems.core.cli.__main__.cbb_stats"></a>

## cbb\_stats

```python
def cbb_stats(fetch_data=True)
```

<a id="ratingsystems.core.cli.__main__.cbb_bracket"></a>

## cbb\_bracket

```python
def cbb_bracket(fetch_data=True)
```

<a id="ratingsystems.core.cli.__main__.cbb_test"></a>

## cbb\_test

```python
def cbb_test(fetch_data=True)
```

<a id="ratingsystems.core.data_source"></a>

# Module ratingsystems.core.data\_source

Defines a data source, which can be used to fetch data for a sport.

A data source can be used by calling the [`fetch`](#ratingsystems.core.cli.cli.fetch) function. This will return a list of [`Game`](#ratingsystems.core.model.game.Game).

This is also exposed via the CLI command `fetch`, which can be called like this:
```bash
ratingsystems fetch --data <datasource>
```

<a id="ratingsystems.core.data_source.DataSource"></a>

## DataSource

```python
class DataSource(ABC)
```

Abstract class used to create a data source.

Classes that inherit from [`DataSource`](#ratingsystems.core.data_source.DataSource) must implement a [`fetch`](#ratingsystems.core.cli.cli.fetch) method which returns a list of [`Game`](#ratingsystems.core.model.game.Game).

Classes that inherit from [`DataSource`](#ratingsystems.core.data_source.DataSource) can accept any options to __init__, but they must have a default value, and it must accept a year (int) as its first argument.

Classes that inherit from [`DataSource`](#ratingsystems.core.data_source.DataSource) should override the name class attribute to give their data source a name.

Classes that inherit from [`DataSource`](#ratingsystems.core.data_source.DataSource) can override the stats_class class attribute (default: [`GameStats`](#ratingsystems.core.model.game.GameStats)) to give their data source a name. The stats_class field is used when loading data from the local disk to convert the stats into the right class.

<a id="ratingsystems.core.data_source.DataSource.name"></a>

### name: `str`

(str) Name of the data source; will be used by the CLI, so ideally this is short

<a id="ratingsystems.core.data_source.DataSource.stats_class"></a>

### stats\_class: `type[GameStats]`

(type[[`GameStats`](#ratingsystems.core.model.game.GameStats)]) Class to use for the game stats; useful if you want to include additional stats for a data source (default: [`GameStats`](#ratingsystems.core.model.game.GameStats))

<a id="ratingsystems.core.data_source.DataSource.fetch"></a>

### fetch

```python
@abstractmethod
def fetch() -> list[Game]
```

Method to fetch game data.

Returns:
    list of [`Game`](#ratingsystems.core.model.game.Game) objects

<a id="ratingsystems.core.data_source.DataSource.save"></a>

### save

```python
def save(games: list[Game])
```

Save game data to local disk.

Args:
    games (list[[`Game`](#ratingsystems.core.model.game.Game)]): list of games

<a id="ratingsystems.core.data_source.DataSource.load"></a>

### load

```python
def load(incomplete: bool = True) -> list[Game]
```

Load game data from local disk.

Returns:
    list of [`Game`](#ratingsystems.core.model.game.Game)

<a id="ratingsystems.core.data_source.DataSource.data_dir"></a>

### data\_dir

```python
@property
def data_dir() -> str
```

<a id="ratingsystems.core.data_source.DataSource.data_path"></a>

### data\_path

```python
@property
def data_path() -> str
```

<a id="ratingsystems.core.data_source.DataSource.auth_token"></a>

### auth\_token

```python
@property
def auth_token() -> str
```

<a id="ratingsystems.core.data_source.DataSource.auth_token"></a>

### auth\_token

```python
@auth_token.setter
def auth_token(value: str)
```

<a id="ratingsystems.core.model.bracket"></a>

# Module ratingsystems.core.model.bracket

<a id="ratingsystems.core.model.bracket.Bracket"></a>

## Bracket

```python
@dataclass
class Bracket()
```

<a id="ratingsystems.core.model.bracket.Bracket.subbracket_1"></a>

### subbracket\_1: `Optional[Any]`

<a id="ratingsystems.core.model.bracket.Bracket.subbracket_2"></a>

### subbracket\_2: `Optional[Any]`

<a id="ratingsystems.core.model.bracket.Bracket.seed_1"></a>

### seed\_1: `Optional[int]`

<a id="ratingsystems.core.model.bracket.Bracket.seed_2"></a>

### seed\_2: `Optional[int]`

<a id="ratingsystems.core.model.bracket.Bracket.bracket_name"></a>

### bracket\_name: `str`

<a id="ratingsystems.core.model.bracket.Bracket.odds"></a>

### odds: `Dict[str, float]`

<a id="ratingsystems.core.model.bracket.Bracket.depth"></a>

### depth

```python
@property
def depth() -> int
```

<a id="ratingsystems.core.model.bracket.Bracket.teams"></a>

### teams

```python
@property
def teams() -> List[str]
```

<a id="ratingsystems.core.model.bracket.Bracket.predicted_team"></a>

### predicted\_team

```python
@property
def predicted_team() -> str
```

<a id="ratingsystems.core.model.bracket.Bracket.evaluate"></a>

### evaluate

```python
def evaluate(predictor: Callable[[str, str], str],
             results: dict[str, int] = {})
```

<a id="ratingsystems.core.model.bracket.Bracket.full_odds"></a>

### full\_odds

```python
@property
def full_odds() -> Dict[str, Tuple[str, str, int, List[float]]]
```

<a id="ratingsystems.core.model.game"></a>

# Module ratingsystems.core.model.game

<a id="ratingsystems.core.model.game.GameStats"></a>

## GameStats

```python
@dataclass
class GameStats()
```

Class representing stats for a team in a game.

Can be inheritted by another class to add more stats.

<a id="ratingsystems.core.model.game.GameStats.points"></a>

### points: `Optional[int]`

(int) Points scored

<a id="ratingsystems.core.model.game.GameStats.period_points"></a>

### period\_points: `list[int]`

(list[int]) Points scored in each period

<a id="ratingsystems.core.model.game.Game"></a>

## Game

```python
@dataclass
class Game()
```

Class representing a game.

<a id="ratingsystems.core.model.game.Game.id"></a>

### id: `int`

(int) Unique id for this game

<a id="ratingsystems.core.model.game.Game.season"></a>

### season: `int`

(int) Season this game was played in

<a id="ratingsystems.core.model.game.Game.home_team"></a>

### home\_team: `str`

(str) Name of the home team

<a id="ratingsystems.core.model.game.Game.away_team"></a>

### away\_team: `str`

(str) Name of the away team

<a id="ratingsystems.core.model.game.Game.preseason"></a>

### preseason: `bool`

(bool) Whether this game was in the preseason (default: False)

<a id="ratingsystems.core.model.game.Game.postseason"></a>

### postseason: `bool`

(bool) Whether this game was in the postseason (default: False)

<a id="ratingsystems.core.model.game.Game.start_date"></a>

### start\_date: `Optional[datetime]`

(datetime) Start date of the game (default: None)

<a id="ratingsystems.core.model.game.Game.neutral_site"></a>

### neutral\_site: `bool`

(bool) Whether this game was played at a neutral site (default: False)

<a id="ratingsystems.core.model.game.Game.conference_game"></a>

### conference\_game: `bool`

(bool) Whether this game was a conference game (default: False)

<a id="ratingsystems.core.model.game.Game.complete"></a>

### complete: `bool`

(bool) Whether this game is complete (default: True)

<a id="ratingsystems.core.model.game.Game.overtime"></a>

### overtime: `bool`

(bool) Whether this game went to overtime (default: False)

<a id="ratingsystems.core.model.game.Game.home_conference"></a>

### home\_conference: `Optional[str]`

(str) Name of the conference of the home team (default: None)

<a id="ratingsystems.core.model.game.Game.home_seed"></a>

### home\_seed: `Optional[int]`

(int) Seed of the home team (default: None)

<a id="ratingsystems.core.model.game.Game.home_points"></a>

### home\_points: `Optional[int]`

(int) Points scored by the home team (default: None)

<a id="ratingsystems.core.model.game.Game.home_period_points"></a>

### home\_period\_points: `list[int]`

(list[int]) Points scored by the home team in each period (default: None)

<a id="ratingsystems.core.model.game.Game.home_winner"></a>

### home\_winner: `Optional[bool]`

(bool) Whether the home team won (default: None)

<a id="ratingsystems.core.model.game.Game.home_stats"></a>

### home\_stats: `Optional[GameStats]`

([`GameStats`](#ratingsystems.core.model.game.GameStats)) Additional stats for the home team (default: None)

<a id="ratingsystems.core.model.game.Game.away_conference"></a>

### away\_conference: `Optional[str]`

(str) Name of the conference of the away team (default: None)

<a id="ratingsystems.core.model.game.Game.away_seed"></a>

### away\_seed: `Optional[int]`

(int) Seed of the away team (default: None)

<a id="ratingsystems.core.model.game.Game.away_points"></a>

### away\_points: `Optional[int]`

(int) Points scored by the away team (default: None)

<a id="ratingsystems.core.model.game.Game.away_period_points"></a>

### away\_period\_points: `list[int]`

(list[int]) Points scored by the away team in each period (default: None)

<a id="ratingsystems.core.model.game.Game.away_winner"></a>

### away\_winner: `Optional[bool]`

(bool) Whether the away team won (default: None)

<a id="ratingsystems.core.model.game.Game.away_stats"></a>

### away\_stats: `Optional[GameStats]`

([`GameStats`](#ratingsystems.core.model.game.GameStats)) Additional stats for the away team (default: None)

<a id="ratingsystems.core.model.game.Game.stats_class"></a>

### stats\_class: `InitVar[Optional[Type[GameStats]]]`

(type[[`GameStats`](#ratingsystems.core.model.game.GameStats)]) Class to use for the game stats; useful if you want to include additional stats for a game (default: [`GameStats`](#ratingsystems.core.model.game.GameStats))

<a id="ratingsystems.core.model.prediction"></a>

# Module ratingsystems.core.model.prediction

<a id="ratingsystems.core.model.prediction.Prediction"></a>

## Prediction

```python
@dataclass
class Prediction()
```

Class representing a prediction.

<a id="ratingsystems.core.model.prediction.Prediction.team"></a>

### team: `str`

(str) Name of the team

<a id="ratingsystems.core.model.prediction.Prediction.opponent"></a>

### opponent: `str`

(str) Name of the opponent

<a id="ratingsystems.core.model.prediction.Prediction.line"></a>

### line: `Optional[float]`

(float) Predicted line of the matchup (default: None)

<a id="ratingsystems.core.model.prediction.Prediction.odds"></a>

### odds: `Optional[float]`

(float) Predicted odds of the matchup (default: None)

<a id="ratingsystems.core.model.prediction.Prediction.team_score"></a>

### team\_score: `Optional[float]`

(float) Predicted score of team in the matchup (default: None)

<a id="ratingsystems.core.model.prediction.Prediction.opponent_score"></a>

### opponent\_score: `Optional[float]`

(float) Predicted score of opponent in the matchup (default: None)

<a id="ratingsystems.core.model.rating"></a>

# Module ratingsystems.core.model.rating

<a id="ratingsystems.core.model.rating.Rating"></a>

## Rating

```python
class Rating()
```

Class representing a rating of teams. This class also provides many helpful functions for interacting with the ratings.

Parameters:
    - rating (dict[str, [`Stat`](#ratingsystems.core.model.stat.Stat)]): mapping of team names to ratings, represented by a [`Stat`](#ratingsystems.core.model.stat.Stat) object
    - games (list[Game]): list of games used to generate this rating
    - name (str): name of the rating; when transforming [`Rating`](#ratingsystems.core.model.rating.Rating) objects through arithmetic operators, [`Rating`](#ratingsystems.core.model.rating.Rating) objects with names will be accessible in the resulting [`Rating`](#ratingsystems.core.model.rating.Rating) object via a property based on the name; names that begin with an underscore will be hidden and will not appear unless explicitly requested (default: None)
    - stat_class (Type[Stat]): Stat type that, if specified, is used to convert ratings (default: None)
    - **auxillary_data: additional fields to be stored on the [`Rating`](#ratingsystems.core.model.rating.Rating); this can be sub rating, additional data needed for a predictor, or anything else useful to a consumer of the rating

All of the arithmetic operators work on [`Rating`](#ratingsystems.core.model.rating.Rating) objects just like regular numbers. The result of these arithmetic operators will be a new [`Rating`](#ratingsystems.core.model.rating.Rating) object that contains the original ratings transformed by the arithmetic operation.
    ```python
    (rating + 1).get_value(team) == rating.get_value(team) + 1
    (2 * rating).get_value(team) == 2 * rating.get_value(team)
    (rating1 - rating2).get_value(team) == rating1.get_value(team) - rating2.get_value(team)
    ```

This can be used to create new ratings that are combinations of existing ratings. For example, it may be useful in a rating system to create simple ratings, then combine and transform these into more complex ratings, without having to do so across all teams. It may also be useful to modify and/or combine ratings from different rating systems.

[`Rating`](#ratingsystems.core.model.rating.Rating) objects with a name will be accessible in the resulting [`Rating`](#ratingsystems.core.model.rating.Rating) object via a property based on the name of the [`Rating`](#ratingsystems.core.model.rating.Rating) object.
    ```python
    named_rating = Rating(data, games, name="abc")
    (rating + 1).abc == named_rating
    ```

The following useful operations can also be achieved using other operators.

You can add or change the name of a [`Rating`](#ratingsystems.core.model.rating.Rating) object using the modulo operator (%)
    ```python
    rating = (rating1 + rating2) % "new_name"
    ```
This can be especially useful when combined with the arithmetic operators to give names to the new ratings you're creating.

You can add a [`Rating`](#ratingsystems.core.model.rating.Rating) object as a sub rating of another [`Rating`](#ratingsystems.core.model.rating.Rating) object using the left shift operator (<<)
    ```python
    rating = (rating1 + rating2) << sub_rating
    ```
This can be useful to add additional ratings that weren't used in calculating your rating. (Note: the sub rating must have a name, otherwise this operation will fail) 

You can cast the ratings of a [`Rating`](#ratingsystems.core.model.rating.Rating) object to a different [`Stat`](#ratingsystems.core.model.stat.Stat) class using the or operator (|)
    ```python
    rating = (rating1 + rating2) | [`Stat`](#ratingsystems.core.model.stat.Stat)
    ```
This can be useful when you are combining two ratings with one [`Stat`](#ratingsystems.core.model.stat.Stat) type, but wish for the resulting rating to be a different [`Stat`](#ratingsystems.core.model.stat.Stat) type.

<a id="ratingsystems.core.model.rating.Rating.get"></a>

### get

```python
def get(team: str) -> Stat
```

<a id="ratingsystems.core.model.rating.Rating.get_value"></a>

### get\_value

```python
def get_value(team: str) -> Number
```

<a id="ratingsystems.core.model.rating.Rating.get_zscore"></a>

### get\_zscore

```python
def get_zscore(team: str) -> Number
```

<a id="ratingsystems.core.model.rating.Rating.get_team"></a>

### get\_team

```python
def get_team(team: str) -> TeamRating
```

<a id="ratingsystems.core.model.rating.Rating.confidence_interval"></a>

### confidence\_interval

```python
@property
def confidence_interval() -> float
```

<a id="ratingsystems.core.model.rating.Rating.mean"></a>

### mean

```python
@property
def mean() -> float
```

<a id="ratingsystems.core.model.rating.Rating.stdev"></a>

### stdev

```python
@property
def stdev() -> float
```

<a id="ratingsystems.core.model.rating.Rating.keys"></a>

### keys

```python
def keys() -> Iterable[str]
```

<a id="ratingsystems.core.model.rating.Rating.teams"></a>

### teams

```python
def teams() -> Iterable[str]
```

<a id="ratingsystems.core.model.rating.Rating.ratings"></a>

### ratings

```python
def ratings(hidden: bool = False) -> Iterable[Self]
```

<a id="ratingsystems.core.model.rating.Rating.rank"></a>

### rank

```python
@staticmethod
def rank(rating: Self, reverse: bool = False) -> list[Tuple[str, Stat]]
```

<a id="ratingsystems.core.model.stat"></a>

# Module ratingsystems.core.model.stat

<a id="ratingsystems.core.model.stat.Stat"></a>

## Stat

```python
class Stat()
```

<a id="ratingsystems.core.model.stat.Stat.formatted"></a>

### formatted

```python
def formatted(precision: int = 1) -> str
```

<a id="ratingsystems.core.model.team_rating"></a>

# Module ratingsystems.core.model.team\_rating

<a id="ratingsystems.core.model.team_rating.TeamRating"></a>

## TeamRating

```python
class TeamRating()
```

<a id="ratingsystems.core.model.team_rating.TeamRating.ratings"></a>

### ratings

```python
def ratings(hidden: bool = False) -> Iterable[Stat]
```

<a id="ratingsystems.core.model.team_rating.TeamRating.combine"></a>

### combine

```python
@staticmethod
def combine(*ratings, rating: Optional[Stat] = None, **sub_ratings)
```

<a id="ratingsystems.core.model"></a>

# Module ratingsystems.core.model

<a id="ratingsystems.core.predictor"></a>

# Module ratingsystems.core.predictor

Defines a predictor, which can be used to predict a matchup between two teams.

A predictor can be used by calling the [`predict`](#ratingsystems.core.cli.__main__.predict) function with a team and an opponent. This will return a [`Prediction`](#ratingsystems.core.model.prediction.Prediction) of the matchup.

This is also exposed via the CLI command `predict`, which can be called like this:
```bash
ratingsystems predict TEAM OPPONENT --data <datasource> --rating <ratingsystem> --predictor <predictor>
```

<a id="ratingsystems.core.predictor.Predictor"></a>

## Predictor

```python
class Predictor(ABC)
```

Abstract class used to create a predictor.

Classes that inherit from [`Predictor`](#ratingsystems.core.predictor.Predictor) must implement a [`predict`](#ratingsystems.core.cli.__main__.predict) method which takes as input a team and an opponent and returns a [`Prediction`](#ratingsystems.core.model.prediction.Prediction) object.

Classes that inherit from [`Predictor`](#ratingsystems.core.predictor.Predictor) can accept any options to __init__, but they must have a default value, and it must accept a [`Rating`](#ratingsystems.core.model.rating.Rating) as its first argument.

Classes that inherit from [`Predictor`](#ratingsystems.core.predictor.Predictor) should override the name class attribute to give their predictor a name.

<a id="ratingsystems.core.predictor.Predictor.name"></a>

### name: `str`

(str) Name of predictor; will be used by the CLI, so ideally this is short

<a id="ratingsystems.core.predictor.Predictor.predict"></a>

### predict

```python
@abstractmethod
def predict(team: str, opponent: str) -> Prediction
```

Method to predict a matchup of two teams.

Args:
    team (str): first team of the matchup
    opponent (str): second team of the matchup

Returns:
    [`Prediction`](#ratingsystems.core.model.prediction.Prediction) object with prediction for the matchup

<a id="ratingsystems.core.predictor.AggregatePredictor"></a>

## AggregatePredictor

```python
class AggregatePredictor()
```

<a id="ratingsystems.core.predictor.AggregatePredictor.predict"></a>

### predict

```python
def predict(team: str, opponent: str) -> Prediction
```

<a id="ratingsystems.core.predictor.RatingDifferencePredictor"></a>

## RatingDifferencePredictor

```python
class RatingDifferencePredictor(Predictor)
```

<a id="ratingsystems.core.predictor.RatingDifferencePredictor.name"></a>

### name: `str`

<a id="ratingsystems.core.predictor.RatingDifferencePredictor.predict"></a>

### predict

```python
def predict(team: str, opponent: str) -> Prediction
```

<a id="ratingsystems.core.rating_system"></a>

# Module ratingsystems.core.rating\_system

Defines a rating system, which can be used to create a rating of teams.

A rating system can be used by calling the [`rate`](#ratingsystems.core.cli.cli.rate) function with a list of [`Game`](#ratingsystems.core.model.game.Game). This will return a [`Rating`](#ratingsystems.core.model.rating.Rating) of the teams.

This is also exposed via the CLI command `rate`, which can be called like this:
```bash
ratingsystems rate --data <datasource> --rating <ratingsystem>
```

<a id="ratingsystems.core.rating_system.RatingSystem"></a>

## RatingSystem

```python
class RatingSystem(ABC)
```

Abstract class used to create a rating system.

Classes that inherit from [`RatingSystem`](#ratingsystems.core.rating_system.RatingSystem) must implement a [`rate`](#ratingsystems.core.cli.cli.rate) method which takes as input a list of [`Game`](#ratingsystems.core.model.game.Game) objects and returns a [`Rating`](#ratingsystems.core.model.rating.Rating) object.

Classes that inherit from [`RatingSystem`](#ratingsystems.core.rating_system.RatingSystem) can accept any options to __init__, but they must have a default value.

Classes that inherit from [`RatingSystem`](#ratingsystems.core.rating_system.RatingSystem) should override the name class attribute to give their rating system a name.

<a id="ratingsystems.core.rating_system.RatingSystem.name"></a>

### name: `str`

(str) Name of the rating system; will be used by the CLI, so ideally this is short

<a id="ratingsystems.core.rating_system.RatingSystem.rate"></a>

### rate

```python
@abstractmethod
def rate(games: list[Game]) -> Rating
```

Method to create a rating based on game data.

Args:
    games (list[[`Game`](#ratingsystems.core.model.game.Game)]): list of games

Returns:
    [`Rating`](#ratingsystems.core.model.rating.Rating) object with a rating for each team found in the game data

<a id="ratingsystems.core.util.file"></a>

# Module ratingsystems.core.util.file

<a id="ratingsystems.core.util.file.config_path"></a>

## config\_path

<a id="ratingsystems.core.util.math"></a>

# Module ratingsystems.core.util.math

<a id="ratingsystems.core.util.math.linear_regression"></a>

## linear\_regression

```python
def linear_regression(X: Union[list[float], list[list[float]]],
                      y: list[float],
                      weights: Optional[list[float]] = None,
                      degree: int = 1,
                      log: bool = False)
```

<a id="ratingsystems.core.util.math.logistic_regression"></a>

## logistic\_regression

```python
def logistic_regression(X: Union[list[float], list[list[float]]],
                        y: list[float],
                        weights: Optional[list[float]] = None,
                        degree: int = 1)
```

<a id="ratingsystems.core.util.math.linear_regression_to_points"></a>

## linear\_regression\_to\_points

```python
def linear_regression_to_points(rating: Rating, games: list) -> Rating
```

<a id="ratingsystems.core.util.text"></a>

# Module ratingsystems.core.util.text

<a id="ratingsystems.core.util.text.center"></a>

## center

```python
def center(text: Any, columns: int) -> str
```

<a id="ratingsystems.core.util.text.ljustify"></a>

## ljustify

```python
def ljustify(text: Any, columns: int) -> str
```

<a id="ratingsystems.core.util.text.rjustify"></a>

## rjustify

```python
def rjustify(text: Any, columns: int) -> str
```

<a id="ratingsystems.core.util"></a>

# Module ratingsystems.core.util

<a id="ratingsystems.core"></a>

# Module ratingsystems.core

