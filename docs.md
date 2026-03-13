<a id="ratingsystems.__version__"></a>

#### \_\_version\_\_

<a id="ratingsystems.core.cli.cli.year"></a>

#### year

<a id="ratingsystems.core.cli.cli.datasource"></a>

#### datasource

<a id="ratingsystems.core.cli.cli.ratingsystem"></a>

#### ratingsystem

<a id="ratingsystems.core.cli.cli.predictor"></a>

#### predictor

<a id="ratingsystems.core.cli.cli.options"></a>

#### options

<a id="ratingsystems.core.cli.cli.load_cli_plugins"></a>

#### load\_cli\_plugins

```python
def load_cli_plugins()
```

<a id="ratingsystems.core.cli.cli.cli"></a>

#### cli

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

#### config

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

#### set\_defaults

```python
def set_defaults(
        context,
        new_parameters: Optional[dict[str, Any]] = None) -> dict[str, Any]
```

<a id="ratingsystems.core.cli.cli.fetch"></a>

#### fetch

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

#### rate

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
         hidden: bool = False,
         options: dict[str, Any] = {})
```

Used to create a rating.

<a id="ratingsystems.core.cli.cli.predict"></a>

#### predict

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

<a id="ratingsystems.core.cli.helpers.combine_key_value_pairs"></a>

#### combine\_key\_value\_pairs

```python
def combine_key_value_pairs(ctx: click.Context, param: click.Parameter,
                            value: tuple[dict[str, Any]]) -> dict[str, Any]
```

<a id="ratingsystems.core.cli.helpers.filter_options"></a>

#### filter\_options

```python
def filter_options(options: dict[str, Any], cls: Type)
```

<a id="ratingsystems.core.cli.helpers.SelectChoice"></a>

## SelectChoice Objects

```python
class SelectChoice(click.Choice)
```

<a id="ratingsystems.core.cli.helpers.SelectChoice.__init__"></a>

#### \_\_init\_\_

```python
def __init__(choices: dict[str, Any], *args, **kwargs)
```

<a id="ratingsystems.core.cli.helpers.SelectChoice.convert"></a>

#### convert

```python
def convert(value: Optional[str] = None,
            param: Optional[click.Parameter] = None,
            ctx: Optional[click.Context] = None) -> Any
```

<a id="ratingsystems.core.cli.helpers.WeightedSelectChoice"></a>

## WeightedSelectChoice Objects

```python
class WeightedSelectChoice(SelectChoice)
```

<a id="ratingsystems.core.cli.helpers.WeightedSelectChoice.convert"></a>

#### convert

```python
def convert(value: Optional[str] = None,
            param: Optional[click.Parameter] = None,
            ctx: Optional[click.Context] = None) -> Any
```

<a id="ratingsystems.core.cli.helpers.KeyValuePair"></a>

## KeyValuePair Objects

```python
class KeyValuePair(click.ParamType)
```

<a id="ratingsystems.core.cli.helpers.KeyValuePair.name"></a>

#### name

<a id="ratingsystems.core.cli.helpers.KeyValuePair.__init__"></a>

#### \_\_init\_\_

```python
def __init__(delimiter: str = "=", default: Optional[Any] = None)
```

<a id="ratingsystems.core.cli.helpers.KeyValuePair.convert"></a>

#### convert

```python
def convert(value: Optional[str] = None,
            param: Optional[click.Parameter] = None,
            ctx: Optional[click.Context] = None) -> dict[str, Any]
```

<a id="ratingsystems.core.cli.helpers.KeyValuePair.get_metavar"></a>

#### get\_metavar

```python
def get_metavar(param: click.Parameter,
                ctx: Optional[click.Context] = None) -> str
```

<a id="ratingsystems.core.cli.__main__.WIN_WEIGHT"></a>

#### WIN\_WEIGHT

<a id="ratingsystems.core.cli.__main__.MAXIMUM_MOV"></a>

#### MAXIMUM\_MOV

<a id="ratingsystems.core.cli.__main__.ALPHA"></a>

#### ALPHA

<a id="ratingsystems.core.cli.__main__.MAXIMUM_ITERATIONS"></a>

#### MAXIMUM\_ITERATIONS

<a id="ratingsystems.core.cli.__main__.cfb"></a>

#### cfb

```python
def cfb(fetch_data=True)
```

<a id="ratingsystems.core.cli.__main__.stats"></a>

#### stats

```python
def stats()
```

<a id="ratingsystems.core.cli.__main__.predict"></a>

#### predict

```python
def predict(fetch_data: bool = True)
```

<a id="ratingsystems.core.cli.__main__.rrs"></a>

#### rrs

```python
def rrs(games: list, win_weight: int = 30)
```

<a id="ratingsystems.core.cli.__main__.rrs_predict"></a>

#### rrs\_predict

```python
def rrs_predict(rating: Rating, team: str, opponent: str)
```

<a id="ratingsystems.core.cli.__main__.rrs_predict_markov_chain"></a>

#### rrs\_predict\_markov\_chain

```python
def rrs_predict_markov_chain(rating: Rating, team: str, opponent: str)
```

<a id="ratingsystems.core.cli.__main__.ser"></a>

#### ser

```python
def ser(games: list, seed: Rating = None, k: float = 8.0)
```

<a id="ratingsystems.core.cli.__main__.ser_predict"></a>

#### ser\_predict

```python
def ser_predict(rating: Rating, team: str, opponent: str)
```

<a id="ratingsystems.core.cli.__main__.ser_predict_total"></a>

#### ser\_predict\_total

```python
def ser_predict_total(rating: Rating, team: str, opponent: str)
```

<a id="ratingsystems.core.cli.__main__.zer"></a>

#### zer

```python
def zer(games: list, seed: Rating = None)
```

<a id="ratingsystems.core.cli.__main__.cer"></a>

#### cer

```python
def cer(games: list, seed: Rating = None)
```

<a id="ratingsystems.core.cli.__main__.cbb"></a>

#### cbb

```python
def cbb(fetch_data=True)
```

<a id="ratingsystems.core.cli.__main__.cbb_stats"></a>

#### cbb\_stats

```python
def cbb_stats(fetch_data=True)
```

<a id="ratingsystems.core.cli.__main__.cbb_bracket"></a>

#### cbb\_bracket

```python
def cbb_bracket(fetch_data=True)
```

<a id="ratingsystems.core.cli.__main__.cbb_test"></a>

#### cbb\_test

```python
def cbb_test(fetch_data=True)
```

Defines a data source, which can be used to fetch data for a sport.

A data source can be used by calling the [`fetch`](ratingsystems.core.cli.cli.fetch) function. This will return a list of [`Game`](ratingsystems.core.model.game.Game).

This is also exposed via the CLI command `fetch`, which can be called like this:
```bash
ratingsystems fetch --data <datasource>
```

<a id="ratingsystems.core.data_source.DataSource"></a>

## DataSource Objects

```python
class DataSource(ABC)
```

Abstract class used to create a data source.

Classes that inherit from [`DataSource`](ratingsystems.core.data_source.DataSource) must implement a [`fetch`](ratingsystems.core.cli.cli.fetch) method which returns a list of [`Game`](ratingsystems.core.model.game.Game).

Classes that inherit from [`DataSource`](ratingsystems.core.data_source.DataSource) can accept any options to __init__, but they must have a default value, and it must accept a year (int) as its first argument.

Classes that inherit from [`DataSource`](ratingsystems.core.data_source.DataSource) should override the name class attribute to give their data source a name.

Classes that inherit from [`DataSource`](ratingsystems.core.data_source.DataSource) can override the stats_class class attribute (default: [`GameStats`](ratingsystems.core.model.game.GameStats)) to give their data source a name. The stats_class field is used when loading data from the local disk to convert the stats into the right class.

<a id="ratingsystems.core.data_source.DataSource.name"></a>

#### name

<a id="ratingsystems.core.data_source.DataSource.stats_class"></a>

#### stats\_class

<a id="ratingsystems.core.data_source.DataSource.__init__"></a>

#### \_\_init\_\_

```python
def __init__(year: int)
```

<a id="ratingsystems.core.data_source.DataSource.fetch"></a>

#### fetch

```python
@abstractmethod
def fetch() -> list[Game]
```

Method to fetch game data.

Returns:
    list of [`Game`](ratingsystems.core.model.game.Game) objects

<a id="ratingsystems.core.data_source.DataSource.save"></a>

#### save

```python
def save(games: list[Game])
```

Save game data to local disk.

Args:
    games (list[[`Game`](ratingsystems.core.model.game.Game)]): list of games

<a id="ratingsystems.core.data_source.DataSource.load"></a>

#### load

```python
def load(incomplete: bool = True) -> list[Game]
```

Load game data from local disk.

Returns:
    list of [`Game`](ratingsystems.core.model.game.Game)

<a id="ratingsystems.core.data_source.DataSource.data_dir"></a>

#### data\_dir

```python
@property
def data_dir() -> str
```

<a id="ratingsystems.core.data_source.DataSource.data_path"></a>

#### data\_path

```python
@property
def data_path() -> str
```

<a id="ratingsystems.core.data_source.DataSource.auth_token"></a>

#### auth\_token

```python
@property
def auth_token() -> str
```

<a id="ratingsystems.core.data_source.DataSource.auth_token"></a>

#### auth\_token

```python
@auth_token.setter
def auth_token(value: str)
```

<a id="ratingsystems.core.data_source.DataSource.__str__"></a>

#### \_\_str\_\_

```python
def __str__() -> str
```

<a id="ratingsystems.core.data_source.DataSource.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="ratingsystems.core.model.bracket.Bracket"></a>

## Bracket Objects

```python
@dataclass
class Bracket()
```

<a id="ratingsystems.core.model.bracket.Bracket.subbracket_1"></a>

#### subbracket\_1

<a id="ratingsystems.core.model.bracket.Bracket.subbracket_2"></a>

#### subbracket\_2

<a id="ratingsystems.core.model.bracket.Bracket.seed_1"></a>

#### seed\_1

<a id="ratingsystems.core.model.bracket.Bracket.seed_2"></a>

#### seed\_2

<a id="ratingsystems.core.model.bracket.Bracket.bracket_name"></a>

#### bracket\_name

<a id="ratingsystems.core.model.bracket.Bracket.odds"></a>

#### odds

<a id="ratingsystems.core.model.bracket.Bracket.depth"></a>

#### depth

```python
@property
def depth() -> int
```

<a id="ratingsystems.core.model.bracket.Bracket.teams"></a>

#### teams

```python
@property
def teams() -> List[str]
```

<a id="ratingsystems.core.model.bracket.Bracket.predicted_team"></a>

#### predicted\_team

```python
@property
def predicted_team() -> str
```

<a id="ratingsystems.core.model.bracket.Bracket.evaluate"></a>

#### evaluate

```python
def evaluate(predictor: Callable[[str, str], str],
             results: dict[str, int] = {})
```

<a id="ratingsystems.core.model.bracket.Bracket.full_odds"></a>

#### full\_odds

```python
@property
def full_odds() -> Dict[str, Tuple[str, str, int, List[float]]]
```

<a id="ratingsystems.core.model.bracket.Bracket.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="ratingsystems.core.model.game.GameStats"></a>

## GameStats Objects

```python
@dataclass
class GameStats()
```

Class that represents stats for a team in a game.

Can be inheritted by another class to add more stats.

    points: int
    period_points: list[int]

<a id="ratingsystems.core.model.game.GameStats.points"></a>

#### points

<a id="ratingsystems.core.model.game.GameStats.period_points"></a>

#### period\_points

<a id="ratingsystems.core.model.game.Game"></a>

## Game Objects

```python
@dataclass
class Game()
```

Class that represents a game.

    id: int
    season: int
    home_team: str
    away_team: str
    preseason: bool
    postseason: bool
    start_date: Optional[datetime]
    neutral_site: bool
    conference_game: bool
    complete: bool
    overtime: bool
    home_conference: Optional[str]
    home_seed: Optional[int]
    home_points: Optional[int]
    home_period_points: list[int]
    home_winner: Optional[bool]
    home_stats: Optional[GameStats]
    away_conference: Optional[str]
    away_seed: Optional[int]
    away_points: Optional[int]
    away_period_points: list[int]
    away_winner: Optional[bool]
    away_stats: Optional[GameStats]
    stats_class: InitVar[Optional[Type[GameStats]]]

<a id="ratingsystems.core.model.game.Game.id"></a>

#### id

<a id="ratingsystems.core.model.game.Game.season"></a>

#### season

<a id="ratingsystems.core.model.game.Game.home_team"></a>

#### home\_team

<a id="ratingsystems.core.model.game.Game.away_team"></a>

#### away\_team

<a id="ratingsystems.core.model.game.Game.preseason"></a>

#### preseason

<a id="ratingsystems.core.model.game.Game.postseason"></a>

#### postseason

<a id="ratingsystems.core.model.game.Game.start_date"></a>

#### start\_date

<a id="ratingsystems.core.model.game.Game.neutral_site"></a>

#### neutral\_site

<a id="ratingsystems.core.model.game.Game.conference_game"></a>

#### conference\_game

<a id="ratingsystems.core.model.game.Game.complete"></a>

#### complete

<a id="ratingsystems.core.model.game.Game.overtime"></a>

#### overtime

<a id="ratingsystems.core.model.game.Game.home_conference"></a>

#### home\_conference

<a id="ratingsystems.core.model.game.Game.home_seed"></a>

#### home\_seed

<a id="ratingsystems.core.model.game.Game.home_points"></a>

#### home\_points

<a id="ratingsystems.core.model.game.Game.home_period_points"></a>

#### home\_period\_points

<a id="ratingsystems.core.model.game.Game.home_winner"></a>

#### home\_winner

<a id="ratingsystems.core.model.game.Game.home_stats"></a>

#### home\_stats

<a id="ratingsystems.core.model.game.Game.away_conference"></a>

#### away\_conference

<a id="ratingsystems.core.model.game.Game.away_seed"></a>

#### away\_seed

<a id="ratingsystems.core.model.game.Game.away_points"></a>

#### away\_points

<a id="ratingsystems.core.model.game.Game.away_period_points"></a>

#### away\_period\_points

<a id="ratingsystems.core.model.game.Game.away_winner"></a>

#### away\_winner

<a id="ratingsystems.core.model.game.Game.away_stats"></a>

#### away\_stats

<a id="ratingsystems.core.model.game.Game.stats_class"></a>

#### stats\_class

<a id="ratingsystems.core.model.game.Game.__post_init__"></a>

#### \_\_post\_init\_\_

```python
def __post_init__(stats_class)
```

<a id="ratingsystems.core.model.prediction.Prediction"></a>

## Prediction Objects

```python
class Prediction()
```

<a id="ratingsystems.core.model.prediction.Prediction.__init__"></a>

#### \_\_init\_\_

```python
def __init__(team: str,
             opponent: str,
             line: Optional[float] = None,
             odds: Optional[float] = None,
             team_score: Optional[float] = None,
             opponent_score: Optional[float] = None)
```

<a id="ratingsystems.core.model.prediction.Prediction.__str__"></a>

#### \_\_str\_\_

```python
def __str__() -> str
```

<a id="ratingsystems.core.model.prediction.Prediction.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="ratingsystems.core.model.rating.Rating"></a>

## Rating Objects

```python
class Rating()
```

<a id="ratingsystems.core.model.rating.Rating.__init__"></a>

#### \_\_init\_\_

```python
def __init__(rating: Union[dict[str, Stat], Any],
             name: str = None,
             games: list = [],
             stat_class: Type[Stat] = None,
             **auxilliary_data)
```

<a id="ratingsystems.core.model.rating.Rating.get"></a>

#### get

```python
def get(team: str) -> Stat
```

<a id="ratingsystems.core.model.rating.Rating.get_value"></a>

#### get\_value

```python
def get_value(team: str) -> Number
```

<a id="ratingsystems.core.model.rating.Rating.get_zscore"></a>

#### get\_zscore

```python
def get_zscore(team: str) -> Number
```

<a id="ratingsystems.core.model.rating.Rating.get_team"></a>

#### get\_team

```python
def get_team(team: str) -> TeamRating
```

<a id="ratingsystems.core.model.rating.Rating.confidence_interval"></a>

#### confidence\_interval

```python
@property
def confidence_interval() -> float
```

<a id="ratingsystems.core.model.rating.Rating.mean"></a>

#### mean

```python
@property
def mean() -> float
```

<a id="ratingsystems.core.model.rating.Rating.stdev"></a>

#### stdev

```python
@property
def stdev() -> float
```

<a id="ratingsystems.core.model.rating.Rating.__iter__"></a>

#### \_\_iter\_\_

```python
def __iter__() -> Iterable[TeamRating]
```

<a id="ratingsystems.core.model.rating.Rating.keys"></a>

#### keys

```python
def keys() -> Iterable[str]
```

<a id="ratingsystems.core.model.rating.Rating.teams"></a>

#### teams

```python
def teams() -> Iterable[str]
```

<a id="ratingsystems.core.model.rating.Rating.ratings"></a>

#### ratings

```python
def ratings(hidden: bool = False) -> Iterable[Self]
```

<a id="ratingsystems.core.model.rating.Rating.__add__"></a>

#### \_\_add\_\_

```python
def __add__(other: Any) -> Self
```

<a id="ratingsystems.core.model.rating.Rating.__radd__"></a>

#### \_\_radd\_\_

```python
def __radd__(other: Any) -> Self
```

<a id="ratingsystems.core.model.rating.Rating.__sub__"></a>

#### \_\_sub\_\_

```python
def __sub__(other: Any) -> Self
```

<a id="ratingsystems.core.model.rating.Rating.__rsub__"></a>

#### \_\_rsub\_\_

```python
def __rsub__(other: Any) -> Self
```

<a id="ratingsystems.core.model.rating.Rating.__mul__"></a>

#### \_\_mul\_\_

```python
def __mul__(other: Any) -> Self
```

<a id="ratingsystems.core.model.rating.Rating.__rmul__"></a>

#### \_\_rmul\_\_

```python
def __rmul__(other: Any) -> Self
```

<a id="ratingsystems.core.model.rating.Rating.__truediv__"></a>

#### \_\_truediv\_\_

```python
def __truediv__(other: Any) -> Self
```

<a id="ratingsystems.core.model.rating.Rating.__rtruediv__"></a>

#### \_\_rtruediv\_\_

```python
def __rtruediv__(other: Any) -> Self
```

<a id="ratingsystems.core.model.rating.Rating.__pow__"></a>

#### \_\_pow\_\_

```python
def __pow__(other: Any) -> Self
```

<a id="ratingsystems.core.model.rating.Rating.__rpow__"></a>

#### \_\_rpow\_\_

```python
def __rpow__(other: Any) -> Self
```

<a id="ratingsystems.core.model.rating.Rating.__abs__"></a>

#### \_\_abs\_\_

```python
def __abs__() -> Self
```

<a id="ratingsystems.core.model.rating.Rating.__mod__"></a>

#### \_\_mod\_\_

```python
def __mod__(other: Any) -> Self
```

<a id="ratingsystems.core.model.rating.Rating.__lshift__"></a>

#### \_\_lshift\_\_

```python
def __lshift__(other: Any) -> Self
```

<a id="ratingsystems.core.model.rating.Rating.__or__"></a>

#### \_\_or\_\_

```python
def __or__(other: Any) -> Self
```

<a id="ratingsystems.core.model.rating.Rating.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="ratingsystems.core.model.rating.Rating.rank"></a>

#### rank

```python
@staticmethod
def rank(rating: Self, reverse: bool = False) -> list[Tuple[str, Stat]]
```

<a id="ratingsystems.core.model.rating._Combination"></a>

## \_Combination Objects

```python
class _Combination(ABC)
```

<a id="ratingsystems.core.model.rating._Combination.__init__"></a>

#### \_\_init\_\_

```python
def __init__(first_rating: Rating,
             second_rating: Union[Rating, Number] = None)
```

<a id="ratingsystems.core.model.rating._Combination.keys"></a>

#### keys

```python
def keys()
```

<a id="ratingsystems.core.model.rating._Combination.get"></a>

#### get

```python
@abstractmethod
def get(team: str) -> Stat
```

<a id="ratingsystems.core.model.rating._Add"></a>

## \_Add Objects

```python
class _Add(_Combination)
```

<a id="ratingsystems.core.model.rating._Add.get"></a>

#### get

```python
def get(team: str) -> Stat
```

<a id="ratingsystems.core.model.rating._Subtract"></a>

## \_Subtract Objects

```python
class _Subtract(_Combination)
```

<a id="ratingsystems.core.model.rating._Subtract.get"></a>

#### get

```python
def get(team: str) -> Stat
```

<a id="ratingsystems.core.model.rating._Multiply"></a>

## \_Multiply Objects

```python
class _Multiply(_Combination)
```

<a id="ratingsystems.core.model.rating._Multiply.get"></a>

#### get

```python
def get(team: str) -> Stat
```

<a id="ratingsystems.core.model.rating._Divide"></a>

## \_Divide Objects

```python
class _Divide(_Combination)
```

<a id="ratingsystems.core.model.rating._Divide.get"></a>

#### get

```python
def get(team: str) -> Stat
```

<a id="ratingsystems.core.model.rating._Pow"></a>

## \_Pow Objects

```python
class _Pow(_Combination)
```

<a id="ratingsystems.core.model.rating._Pow.get"></a>

#### get

```python
def get(team: str) -> Stat
```

<a id="ratingsystems.core.model.rating._AbsoluteValue"></a>

## \_AbsoluteValue Objects

```python
class _AbsoluteValue(_Combination)
```

<a id="ratingsystems.core.model.rating._AbsoluteValue.get"></a>

#### get

```python
def get(team: str) -> Stat
```

<a id="ratingsystems.core.model.stat.Stat"></a>

## Stat Objects

```python
class Stat()
```

<a id="ratingsystems.core.model.stat.Stat.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: float)
```

<a id="ratingsystems.core.model.stat.Stat.formatted"></a>

#### formatted

```python
def formatted(precision: int = 1) -> str
```

<a id="ratingsystems.core.model.stat.Stat.__str__"></a>

#### \_\_str\_\_

```python
def __str__() -> str
```

<a id="ratingsystems.core.model.stat.Stat.__format__"></a>

#### \_\_format\_\_

```python
def __format__(format_spec) -> str
```

<a id="ratingsystems.core.model.stat.Stat.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="ratingsystems.core.model.stat.Stat.__add__"></a>

#### \_\_add\_\_

```python
def __add__(other: Any) -> Self
```

<a id="ratingsystems.core.model.stat.Stat.__radd__"></a>

#### \_\_radd\_\_

```python
def __radd__(other: Any) -> Self
```

<a id="ratingsystems.core.model.stat.Stat.__sub__"></a>

#### \_\_sub\_\_

```python
def __sub__(other: Any) -> Self
```

<a id="ratingsystems.core.model.stat.Stat.__rsub__"></a>

#### \_\_rsub\_\_

```python
def __rsub__(other: Any) -> Self
```

<a id="ratingsystems.core.model.stat.Stat.__mul__"></a>

#### \_\_mul\_\_

```python
def __mul__(other: Any) -> Self
```

<a id="ratingsystems.core.model.stat.Stat.__rmul__"></a>

#### \_\_rmul\_\_

```python
def __rmul__(other: Any) -> Self
```

<a id="ratingsystems.core.model.stat.Stat.__truediv__"></a>

#### \_\_truediv\_\_

```python
def __truediv__(other: Any) -> Self
```

<a id="ratingsystems.core.model.stat.Stat.__rtruediv__"></a>

#### \_\_rtruediv\_\_

```python
def __rtruediv__(other: Any) -> Self
```

<a id="ratingsystems.core.model.stat.Stat.__pow__"></a>

#### \_\_pow\_\_

```python
def __pow__(other: Any) -> Self
```

<a id="ratingsystems.core.model.stat.Stat.__rpow__"></a>

#### \_\_rpow\_\_

```python
def __rpow__(other: Any) -> Self
```

<a id="ratingsystems.core.model.stat.Stat.__abs__"></a>

#### \_\_abs\_\_

```python
def __abs__() -> Self
```

<a id="ratingsystems.core.model.team_rating.TeamRating"></a>

## TeamRating Objects

```python
class TeamRating()
```

<a id="ratingsystems.core.model.team_rating.TeamRating.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name: str,
             rating: Stat,
             wins: int = 0,
             losses: int = 0,
             ties: int = 0,
             **sub_ratings)
```

<a id="ratingsystems.core.model.team_rating.TeamRating.__str__"></a>

#### \_\_str\_\_

```python
def __str__() -> str
```

<a id="ratingsystems.core.model.team_rating.TeamRating.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="ratingsystems.core.model.team_rating.TeamRating.ratings"></a>

#### ratings

```python
def ratings(hidden: bool = False) -> Iterable[Stat]
```

<a id="ratingsystems.core.model.team_rating.TeamRating.combine"></a>

#### combine

```python
@staticmethod
def combine(*ratings, rating: Optional[Stat] = None, **sub_ratings)
```

Defines a predictor, which can be used to predict a matchup between two teams.

A predictor can be used by calling the [`predict`](ratingsystems.core.cli.__main__.predict) function with a team and an opponent. This will return a [`Prediction`](ratingsystems.core.model.prediction.Prediction) of the matchup.

This is also exposed via the CLI command `predict`, which can be called like this:
```bash
ratingsystems predict TEAM OPPONENT --data <datasource> --rating <ratingsystem> --predictor <predictor>
```

<a id="ratingsystems.core.predictor.Predictor"></a>

## Predictor Objects

```python
class Predictor(ABC)
```

Abstract class used to create a predictor.

Classes that inherit from [`Predictor`](ratingsystems.core.predictor.Predictor) must implement a [`predict`](ratingsystems.core.cli.__main__.predict) method which takes as input a team and an opponent and returns a [`Prediction`](ratingsystems.core.model.prediction.Prediction) object.

Classes that inherit from [`Predictor`](ratingsystems.core.predictor.Predictor) can accept any options to __init__, but they must have a default value, and it must accept a [`Rating`](ratingsystems.core.model.rating.Rating) as its first argument.

Classes that inherit from [`Predictor`](ratingsystems.core.predictor.Predictor) should override the name class attribute to give their predictor a name.

<a id="ratingsystems.core.predictor.Predictor.name"></a>

#### name

<a id="ratingsystems.core.predictor.Predictor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(rating: Rating)
```

<a id="ratingsystems.core.predictor.Predictor.predict"></a>

#### predict

```python
@abstractmethod
def predict(team: str, opponent: str) -> Prediction
```

Method to predict a matchup of two teams.

Args:
    team (str): first team of the matchup
    opponent (str): second team of the matchup

Returns:
    [`Prediction`](ratingsystems.core.model.prediction.Prediction) object with prediction for the matchup

<a id="ratingsystems.core.predictor.Predictor.__str__"></a>

#### \_\_str\_\_

```python
def __str__() -> str
```

<a id="ratingsystems.core.predictor.Predictor.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="ratingsystems.core.predictor.AggregatePredictor"></a>

## AggregatePredictor Objects

```python
class AggregatePredictor()
```

<a id="ratingsystems.core.predictor.AggregatePredictor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(*predictors: list[Predictor],
             weights: Optional[list[float]] = None)
```

<a id="ratingsystems.core.predictor.AggregatePredictor.predict"></a>

#### predict

```python
def predict(team: str, opponent: str) -> Prediction
```

<a id="ratingsystems.core.predictor.AggregatePredictor._average"></a>

#### \_average

```python
def _average(values: list[float]) -> float
```

<a id="ratingsystems.core.predictor.RatingDifferencePredictor"></a>

## RatingDifferencePredictor Objects

```python
class RatingDifferencePredictor(Predictor)
```

<a id="ratingsystems.core.predictor.RatingDifferencePredictor.name"></a>

#### name

<a id="ratingsystems.core.predictor.RatingDifferencePredictor.predict"></a>

#### predict

```python
def predict(team: str, opponent: str) -> Prediction
```

Defines a rating system, which can be used to create a rating of teams.

A rating system can be used by calling the [`rate`](ratingsystems.core.cli.cli.rate) function with a list of [`Game`](ratingsystems.core.model.game.Game). This will return a [`Rating`](ratingsystems.core.model.rating.Rating) of the teams.

This is also exposed via the CLI command `rate`, which can be called like this:
```bash
ratingsystems rate --data <datasource> --rating <ratingsystem>
```

<a id="ratingsystems.core.rating_system.RatingSystem"></a>

## RatingSystem Objects

```python
class RatingSystem(ABC)
```

Abstract class used to create a rating system.

Classes that inherit from [`RatingSystem`](ratingsystems.core.rating_system.RatingSystem) must implement a [`rate`](ratingsystems.core.cli.cli.rate) method which takes as input a list of [`Game`](ratingsystems.core.model.game.Game) objects and returns a [`Rating`](ratingsystems.core.model.rating.Rating) object.

Classes that inherit from [`RatingSystem`](ratingsystems.core.rating_system.RatingSystem) can accept any options to __init__, but they must have a default value.

Classes that inherit from [`RatingSystem`](ratingsystems.core.rating_system.RatingSystem) should override the name class attribute to give their rating system a name.

<a id="ratingsystems.core.rating_system.RatingSystem.name"></a>

#### name

<a id="ratingsystems.core.rating_system.RatingSystem.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

<a id="ratingsystems.core.rating_system.RatingSystem.rate"></a>

#### rate

```python
@abstractmethod
def rate(games: list[Game]) -> Rating
```

Method to create a rating based on game data.

Args:
    games (list[[`Game`](ratingsystems.core.model.game.Game)]): list of games

Returns:
    [`Rating`](ratingsystems.core.model.rating.Rating) object with a rating for each team found in the game data

<a id="ratingsystems.core.rating_system.RatingSystem.__str__"></a>

#### \_\_str\_\_

```python
def __str__() -> str
```

<a id="ratingsystems.core.rating_system.RatingSystem.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="ratingsystems.core.util.file.config_path"></a>

#### config\_path

<a id="ratingsystems.core.util.math.linear_regression"></a>

#### linear\_regression

```python
def linear_regression(X: Union[list[float], list[list[float]]],
                      y: list[float],
                      weights: Optional[list[float]] = None,
                      degree: int = 1,
                      log: bool = False)
```

<a id="ratingsystems.core.util.math.logistic_regression"></a>

#### logistic\_regression

```python
def logistic_regression(X: Union[list[float], list[list[float]]],
                        y: list[float],
                        weights: Optional[list[float]] = None,
                        degree: int = 1)
```

<a id="ratingsystems.core.util.math.linear_regression_to_points"></a>

#### linear\_regression\_to\_points

```python
def linear_regression_to_points(rating: Rating, games: list) -> Rating
```

<a id="ratingsystems.core.util.text.center"></a>

#### center

```python
def center(text: Any, columns: int) -> str
```

<a id="ratingsystems.core.util.text.ljustify"></a>

#### ljustify

```python
def ljustify(text: Any, columns: int) -> str
```

<a id="ratingsystems.core.util.text.rjustify"></a>

#### rjustify

```python
def rjustify(text: Any, columns: int) -> str
```

