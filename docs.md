# Table of Contents

* [ratingsystems](#ratingsystems)
  * [AggregatePredictor](#ratingsystems.AggregatePredictor)
  * [Bracket](#ratingsystems.Bracket)
  * [DataSource](#ratingsystems.DataSource)
  * [Game](#ratingsystems.Game)
  * [GameStats](#ratingsystems.GameStats)
  * [Prediction](#ratingsystems.Prediction)
  * [Predictor](#ratingsystems.Predictor)
  * [Rating](#ratingsystems.Rating)
  * [RatingDifferencePredictor](#ratingsystems.RatingDifferencePredictor)
  * [RatingSystem](#ratingsystems.RatingSystem)
  * [Stat](#ratingsystems.Stat)
  * [TeamRating](#ratingsystems.TeamRating)
* [ratingsystems.core.cli.cli](#ratingsystems.core.cli.cli)
  * [inspect](#ratingsystems.core.cli.cli.inspect)
  * [pkgutil](#ratingsystems.core.cli.cli.pkgutil)
  * [entry\_points](#ratingsystems.core.cli.cli.entry_points)
  * [ABC](#ratingsystems.core.cli.cli.ABC)
  * [abstractmethod](#ratingsystems.core.cli.cli.abstractmethod)
  * [datetime](#ratingsystems.core.cli.cli.datetime)
  * [isclass](#ratingsystems.core.cli.cli.isclass)
  * [signature](#ratingsystems.core.cli.cli.signature)
  * [Any](#ratingsystems.core.cli.cli.Any)
  * [Optional](#ratingsystems.core.cli.cli.Optional)
  * [click](#ratingsystems.core.cli.cli.click)
  * [shell](#ratingsystems.core.cli.cli.shell)
  * [ParameterSource](#ratingsystems.core.cli.cli.ParameterSource)
  * [DataSource](#ratingsystems.core.cli.cli.DataSource)
  * [Predictor](#ratingsystems.core.cli.cli.Predictor)
  * [RatingSystem](#ratingsystems.core.cli.cli.RatingSystem)
  * [KeyValuePair](#ratingsystems.core.cli.cli.KeyValuePair)
  * [SelectChoice](#ratingsystems.core.cli.cli.SelectChoice)
  * [combine\_key\_value\_pairs](#ratingsystems.core.cli.cli.combine_key_value_pairs)
  * [filter\_options](#ratingsystems.core.cli.cli.filter_options)
  * [Rating](#ratingsystems.core.cli.cli.Rating)
  * [center](#ratingsystems.core.cli.cli.center)
  * [ljustify](#ratingsystems.core.cli.cli.ljustify)
  * [rjustify](#ratingsystems.core.cli.cli.rjustify)
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
  * [signature](#ratingsystems.core.cli.helpers.signature)
  * [Any](#ratingsystems.core.cli.helpers.Any)
  * [Optional](#ratingsystems.core.cli.helpers.Optional)
  * [Type](#ratingsystems.core.cli.helpers.Type)
  * [click](#ratingsystems.core.cli.helpers.click)
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
  * [cli](#ratingsystems.core.cli.cli)
* [ratingsystems.core.cli.\_\_main\_\_](#ratingsystems.core.cli.__main__)
  * [cbbd](#ratingsystems.core.cli.__main__.cbbd)
  * [cfbd](#ratingsystems.core.cli.__main__.cfbd)
  * [math](#ratingsystems.core.cli.__main__.math)
  * [nx](#ratingsystems.core.cli.__main__.nx)
  * [np](#ratingsystems.core.cli.__main__.np)
  * [pickle](#ratingsystems.core.cli.__main__.pickle)
  * [mean](#ratingsystems.core.cli.__main__.mean)
  * [median](#ratingsystems.core.cli.__main__.median)
  * [click](#ratingsystems.core.cli.__main__.click)
  * [shell](#ratingsystems.core.cli.__main__.shell)
  * [Bracket](#ratingsystems.core.cli.__main__.Bracket)
  * [Rating](#ratingsystems.core.cli.__main__.Rating)
  * [AggregatePredictor](#ratingsystems.core.cli.__main__.AggregatePredictor)
  * [RatingDifferencePredictor](#ratingsystems.core.cli.__main__.RatingDifferencePredictor)
  * [CompleteEfficiencyRatingSystem](#ratingsystems.core.cli.__main__.CompleteEfficiencyRatingSystem)
  * [CompleteEfficiencyRatingPredictor](#ratingsystems.core.cli.__main__.CompleteEfficiencyRatingPredictor)
  * [RelativeRatingSystem](#ratingsystems.core.cli.__main__.RelativeRatingSystem)
  * [RelativeRatingSystemMarkovChainPredictor](#ratingsystems.core.cli.__main__.RelativeRatingSystemMarkovChainPredictor)
  * [PageRank](#ratingsystems.core.cli.__main__.PageRank)
  * [SimpleEfficiencyRatingSystem](#ratingsystems.core.cli.__main__.SimpleEfficiencyRatingSystem)
  * [SimpleEfficiencyPredictor](#ratingsystems.core.cli.__main__.SimpleEfficiencyPredictor)
  * [ZscoreEfficiencyRatingSystem](#ratingsystems.core.cli.__main__.ZscoreEfficiencyRatingSystem)
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
  * [json](#ratingsystems.core.data_source.json)
  * [os](#ratingsystems.core.data_source.os)
  * [ABC](#ratingsystems.core.data_source.ABC)
  * [abstractmethod](#ratingsystems.core.data_source.abstractmethod)
  * [asdict](#ratingsystems.core.data_source.asdict)
  * [Type](#ratingsystems.core.data_source.Type)
  * [Game](#ratingsystems.core.data_source.Game)
  * [GameStat](#ratingsystems.core.data_source.GameStat)
  * [config\_path](#ratingsystems.core.data_source.config_path)
  * [DataSource](#ratingsystems.core.data_source.DataSource)
    * [fetch](#ratingsystems.core.data_source.DataSource.fetch)
    * [save](#ratingsystems.core.data_source.DataSource.save)
    * [load](#ratingsystems.core.data_source.DataSource.load)
    * [data\_dir](#ratingsystems.core.data_source.DataSource.data_dir)
    * [data\_path](#ratingsystems.core.data_source.DataSource.data_path)
    * [auth\_token](#ratingsystems.core.data_source.DataSource.auth_token)
    * [auth\_token](#ratingsystems.core.data_source.DataSource.auth_token)
    * [Meta](#ratingsystems.core.data_source.DataSource.Meta)
* [ratingsystems.core.model.bracket](#ratingsystems.core.model.bracket)
  * [dataclass](#ratingsystems.core.model.bracket.dataclass)
  * [Any](#ratingsystems.core.model.bracket.Any)
  * [Callable](#ratingsystems.core.model.bracket.Callable)
  * [Dict](#ratingsystems.core.model.bracket.Dict)
  * [List](#ratingsystems.core.model.bracket.List)
  * [Optional](#ratingsystems.core.model.bracket.Optional)
  * [Tuple](#ratingsystems.core.model.bracket.Tuple)
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
  * [dataclass](#ratingsystems.core.model.game.dataclass)
  * [field](#ratingsystems.core.model.game.field)
  * [InitVar](#ratingsystems.core.model.game.InitVar)
  * [datetime](#ratingsystems.core.model.game.datetime)
  * [Any](#ratingsystems.core.model.game.Any)
  * [Optional](#ratingsystems.core.model.game.Optional)
  * [Type](#ratingsystems.core.model.game.Type)
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
  * [Optional](#ratingsystems.core.model.prediction.Optional)
  * [Prediction](#ratingsystems.core.model.prediction.Prediction)
* [ratingsystems.core.model.rating](#ratingsystems.core.model.rating)
  * [functools](#ratingsystems.core.model.rating.functools)
  * [math](#ratingsystems.core.model.rating.math)
  * [np](#ratingsystems.core.model.rating.np)
  * [ABC](#ratingsystems.core.model.rating.ABC)
  * [abstractmethod](#ratingsystems.core.model.rating.abstractmethod)
  * [Iterable](#ratingsystems.core.model.rating.Iterable)
  * [Enum](#ratingsystems.core.model.rating.Enum)
  * [Number](#ratingsystems.core.model.rating.Number)
  * [stdev](#ratingsystems.core.model.rating.stdev)
  * [Any](#ratingsystems.core.model.rating.Any)
  * [Optional](#ratingsystems.core.model.rating.Optional)
  * [Self](#ratingsystems.core.model.rating.Self)
  * [Union](#ratingsystems.core.model.rating.Union)
  * [Tuple](#ratingsystems.core.model.rating.Tuple)
  * [Type](#ratingsystems.core.model.rating.Type)
  * [Prediction](#ratingsystems.core.model.rating.Prediction)
  * [TeamRating](#ratingsystems.core.model.rating.TeamRating)
  * [Stat](#ratingsystems.core.model.rating.Stat)
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
  * [Number](#ratingsystems.core.model.stat.Number)
  * [Any](#ratingsystems.core.model.stat.Any)
  * [Self](#ratingsystems.core.model.stat.Self)
  * [Stat](#ratingsystems.core.model.stat.Stat)
    * [formatted](#ratingsystems.core.model.stat.Stat.formatted)
* [ratingsystems.core.model.team\_rating](#ratingsystems.core.model.team_rating)
  * [Iterable](#ratingsystems.core.model.team_rating.Iterable)
  * [Optional](#ratingsystems.core.model.team_rating.Optional)
  * [Self](#ratingsystems.core.model.team_rating.Self)
  * [Stat](#ratingsystems.core.model.team_rating.Stat)
  * [TeamRating](#ratingsystems.core.model.team_rating.TeamRating)
    * [ratings](#ratingsystems.core.model.team_rating.TeamRating.ratings)
    * [combine](#ratingsystems.core.model.team_rating.TeamRating.combine)
* [ratingsystems.core.model](#ratingsystems.core.model)
  * [Bracket](#ratingsystems.core.model.Bracket)
  * [Game](#ratingsystems.core.model.Game)
  * [GameStats](#ratingsystems.core.model.GameStats)
  * [Prediction](#ratingsystems.core.model.Prediction)
  * [Rating](#ratingsystems.core.model.Rating)
  * [Stat](#ratingsystems.core.model.Stat)
  * [TeamRating](#ratingsystems.core.model.TeamRating)
* [ratingsystems.core.predictor](#ratingsystems.core.predictor)
  * [st](#ratingsystems.core.predictor.st)
  * [ABC](#ratingsystems.core.predictor.ABC)
  * [abstractmethod](#ratingsystems.core.predictor.abstractmethod)
  * [signature](#ratingsystems.core.predictor.signature)
  * [Optional](#ratingsystems.core.predictor.Optional)
  * [click](#ratingsystems.core.predictor.click)
  * [ParameterSource](#ratingsystems.core.predictor.ParameterSource)
  * [Prediction](#ratingsystems.core.predictor.Prediction)
  * [Rating](#ratingsystems.core.predictor.Rating)
  * [Predictor](#ratingsystems.core.predictor.Predictor)
    * [predict](#ratingsystems.core.predictor.Predictor.predict)
    * [Meta](#ratingsystems.core.predictor.Predictor.Meta)
  * [AggregatePredictor](#ratingsystems.core.predictor.AggregatePredictor)
    * [predict](#ratingsystems.core.predictor.AggregatePredictor.predict)
  * [RatingDifferencePredictor](#ratingsystems.core.predictor.RatingDifferencePredictor)
    * [predict](#ratingsystems.core.predictor.RatingDifferencePredictor.predict)
* [ratingsystems.core.rating\_system](#ratingsystems.core.rating_system)
  * [ABC](#ratingsystems.core.rating_system.ABC)
  * [abstractmethod](#ratingsystems.core.rating_system.abstractmethod)
  * [signature](#ratingsystems.core.rating_system.signature)
  * [click](#ratingsystems.core.rating_system.click)
  * [ParameterSource](#ratingsystems.core.rating_system.ParameterSource)
  * [Game](#ratingsystems.core.rating_system.Game)
  * [Rating](#ratingsystems.core.rating_system.Rating)
  * [RatingSystem](#ratingsystems.core.rating_system.RatingSystem)
    * [rate](#ratingsystems.core.rating_system.RatingSystem.rate)
    * [Meta](#ratingsystems.core.rating_system.RatingSystem.Meta)
* [ratingsystems.core.util.file](#ratingsystems.core.util.file)
  * [os](#ratingsystems.core.util.file.os)
  * [config\_path](#ratingsystems.core.util.file.config_path)
* [ratingsystems.core.util.math](#ratingsystems.core.util.math)
  * [np](#ratingsystems.core.util.math.np)
  * [LinearRegression](#ratingsystems.core.util.math.LinearRegression)
  * [LogisticRegression](#ratingsystems.core.util.math.LogisticRegression)
  * [PolynomialFeatures](#ratingsystems.core.util.math.PolynomialFeatures)
  * [Optional](#ratingsystems.core.util.math.Optional)
  * [Union](#ratingsystems.core.util.math.Union)
  * [Rating](#ratingsystems.core.util.math.Rating)
  * [Stat](#ratingsystems.core.util.math.Stat)
  * [linear\_regression](#ratingsystems.core.util.math.linear_regression)
  * [logistic\_regression](#ratingsystems.core.util.math.logistic_regression)
  * [linear\_regression\_to\_points](#ratingsystems.core.util.math.linear_regression_to_points)
* [ratingsystems.core.util.text](#ratingsystems.core.util.text)
  * [math](#ratingsystems.core.util.text.math)
  * [Any](#ratingsystems.core.util.text.Any)
  * [center](#ratingsystems.core.util.text.center)
  * [ljustify](#ratingsystems.core.util.text.ljustify)
  * [rjustify](#ratingsystems.core.util.text.rjustify)
* [ratingsystems.core.util](#ratingsystems.core.util)
  * [config\_path](#ratingsystems.core.util.config_path)
  * [linear\_regression](#ratingsystems.core.util.linear_regression)
  * [linear\_regression\_to\_points](#ratingsystems.core.util.linear_regression_to_points)
  * [logistic\_regression](#ratingsystems.core.util.logistic_regression)
  * [center](#ratingsystems.core.util.center)
  * [ljustify](#ratingsystems.core.util.ljustify)
  * [rjustify](#ratingsystems.core.util.rjustify)
* [ratingsystems.core](#ratingsystems.core)
  * [DataSource](#ratingsystems.core.DataSource)
  * [Bracket](#ratingsystems.core.Bracket)
  * [Game](#ratingsystems.core.Game)
  * [GameStats](#ratingsystems.core.GameStats)
  * [Prediction](#ratingsystems.core.Prediction)
  * [Rating](#ratingsystems.core.Rating)
  * [Stat](#ratingsystems.core.Stat)
  * [TeamRating](#ratingsystems.core.TeamRating)
  * [AggregatePredictor](#ratingsystems.core.AggregatePredictor)
  * [Predictor](#ratingsystems.core.Predictor)
  * [RatingDifferencePredictor](#ratingsystems.core.RatingDifferencePredictor)
  * [RatingSystem](#ratingsystems.core.RatingSystem)

<a id="ratingsystems"></a>

# ratingsystems

<a id="ratingsystems.AggregatePredictor"></a>

## AggregatePredictor

<a id="ratingsystems.Bracket"></a>

## Bracket

<a id="ratingsystems.DataSource"></a>

## DataSource

<a id="ratingsystems.Game"></a>

## Game

<a id="ratingsystems.GameStats"></a>

## GameStats

<a id="ratingsystems.Prediction"></a>

## Prediction

<a id="ratingsystems.Predictor"></a>

## Predictor

<a id="ratingsystems.Rating"></a>

## Rating

<a id="ratingsystems.RatingDifferencePredictor"></a>

## RatingDifferencePredictor

<a id="ratingsystems.RatingSystem"></a>

## RatingSystem

<a id="ratingsystems.Stat"></a>

## Stat

<a id="ratingsystems.TeamRating"></a>

## TeamRating

<a id="ratingsystems.core.cli.cli"></a>

# ratingsystems.core.cli.cli

<a id="ratingsystems.core.cli.cli.inspect"></a>

## inspect

<a id="ratingsystems.core.cli.cli.pkgutil"></a>

## pkgutil

<a id="ratingsystems.core.cli.cli.entry_points"></a>

## entry\_points

<a id="ratingsystems.core.cli.cli.ABC"></a>

## ABC

<a id="ratingsystems.core.cli.cli.abstractmethod"></a>

## abstractmethod

<a id="ratingsystems.core.cli.cli.datetime"></a>

## datetime

<a id="ratingsystems.core.cli.cli.isclass"></a>

## isclass

<a id="ratingsystems.core.cli.cli.signature"></a>

## signature

<a id="ratingsystems.core.cli.cli.Any"></a>

## Any

<a id="ratingsystems.core.cli.cli.Optional"></a>

## Optional

<a id="ratingsystems.core.cli.cli.click"></a>

## click

<a id="ratingsystems.core.cli.cli.shell"></a>

## shell

<a id="ratingsystems.core.cli.cli.ParameterSource"></a>

## ParameterSource

<a id="ratingsystems.core.cli.cli.DataSource"></a>

## DataSource

<a id="ratingsystems.core.cli.cli.Predictor"></a>

## Predictor

<a id="ratingsystems.core.cli.cli.RatingSystem"></a>

## RatingSystem

<a id="ratingsystems.core.cli.cli.KeyValuePair"></a>

## KeyValuePair

<a id="ratingsystems.core.cli.cli.SelectChoice"></a>

## SelectChoice

<a id="ratingsystems.core.cli.cli.combine_key_value_pairs"></a>

## combine\_key\_value\_pairs

<a id="ratingsystems.core.cli.cli.filter_options"></a>

## filter\_options

<a id="ratingsystems.core.cli.cli.Rating"></a>

## Rating

<a id="ratingsystems.core.cli.cli.center"></a>

## center

<a id="ratingsystems.core.cli.cli.ljustify"></a>

## ljustify

<a id="ratingsystems.core.cli.cli.rjustify"></a>

## rjustify

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

<a id="ratingsystems.core.cli.helpers"></a>

# ratingsystems.core.cli.helpers

<a id="ratingsystems.core.cli.helpers.signature"></a>

## signature

<a id="ratingsystems.core.cli.helpers.Any"></a>

## Any

<a id="ratingsystems.core.cli.helpers.Optional"></a>

## Optional

<a id="ratingsystems.core.cli.helpers.Type"></a>

## Type

<a id="ratingsystems.core.cli.helpers.click"></a>

## click

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

## SelectChoice

```python
class SelectChoice(click.Choice)
```

<a id="ratingsystems.core.cli.helpers.SelectChoice.convert"></a>

#### convert

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

#### convert

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

#### name

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

<a id="ratingsystems.core.cli"></a>

# ratingsystems.core.cli

<a id="ratingsystems.core.cli.cli"></a>

## cli

<a id="ratingsystems.core.cli.__main__"></a>

# ratingsystems.core.cli.\_\_main\_\_

<a id="ratingsystems.core.cli.__main__.cbbd"></a>

## cbbd

<a id="ratingsystems.core.cli.__main__.cfbd"></a>

## cfbd

<a id="ratingsystems.core.cli.__main__.math"></a>

## math

<a id="ratingsystems.core.cli.__main__.nx"></a>

## nx

<a id="ratingsystems.core.cli.__main__.np"></a>

## np

<a id="ratingsystems.core.cli.__main__.pickle"></a>

## pickle

<a id="ratingsystems.core.cli.__main__.mean"></a>

## mean

<a id="ratingsystems.core.cli.__main__.median"></a>

## median

<a id="ratingsystems.core.cli.__main__.click"></a>

## click

<a id="ratingsystems.core.cli.__main__.shell"></a>

## shell

<a id="ratingsystems.core.cli.__main__.Bracket"></a>

## Bracket

<a id="ratingsystems.core.cli.__main__.Rating"></a>

## Rating

<a id="ratingsystems.core.cli.__main__.AggregatePredictor"></a>

## AggregatePredictor

<a id="ratingsystems.core.cli.__main__.RatingDifferencePredictor"></a>

## RatingDifferencePredictor

<a id="ratingsystems.core.cli.__main__.CompleteEfficiencyRatingSystem"></a>

## CompleteEfficiencyRatingSystem

<a id="ratingsystems.core.cli.__main__.CompleteEfficiencyRatingPredictor"></a>

## CompleteEfficiencyRatingPredictor

<a id="ratingsystems.core.cli.__main__.RelativeRatingSystem"></a>

## RelativeRatingSystem

<a id="ratingsystems.core.cli.__main__.RelativeRatingSystemMarkovChainPredictor"></a>

## RelativeRatingSystemMarkovChainPredictor

<a id="ratingsystems.core.cli.__main__.PageRank"></a>

## PageRank

<a id="ratingsystems.core.cli.__main__.SimpleEfficiencyRatingSystem"></a>

## SimpleEfficiencyRatingSystem

<a id="ratingsystems.core.cli.__main__.SimpleEfficiencyPredictor"></a>

## SimpleEfficiencyPredictor

<a id="ratingsystems.core.cli.__main__.ZscoreEfficiencyRatingSystem"></a>

## ZscoreEfficiencyRatingSystem

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

<a id="ratingsystems.core.data_source"></a>

# ratingsystems.core.data\_source

Defines a data source, which can be used to fetch data for a sport.

A data source can be used by calling the [`DataSource.fetch`](#ratingsystems.core.data_source.DataSource.fetch) function. This will return a list of [`Game`](#ratingsystems.core.data_source.Game).

This is also exposed via the CLI command `fetch`, which can be called like this:
```bash
ratingsystems fetch --data <datasource>
```

<a id="ratingsystems.core.data_source.json"></a>

## json

<a id="ratingsystems.core.data_source.os"></a>

## os

<a id="ratingsystems.core.data_source.ABC"></a>

## ABC

<a id="ratingsystems.core.data_source.abstractmethod"></a>

## abstractmethod

<a id="ratingsystems.core.data_source.asdict"></a>

## asdict

<a id="ratingsystems.core.data_source.Type"></a>

## Type

<a id="ratingsystems.core.data_source.Game"></a>

## Game

<a id="ratingsystems.core.data_source.GameStat"></a>

## GameStat

<a id="ratingsystems.core.data_source.config_path"></a>

## config\_path

<a id="ratingsystems.core.data_source.DataSource"></a>

## DataSource

```python
class DataSource(ABC)
```

Abstract class used to create a data source.

Classes that inherit from [`DataSource`](#ratingsystems.core.data_source.DataSource) must implement a [`fetch`](#ratingsystems.core.data_source.DataSource.fetch) method which returns a list of [`Game`](#ratingsystems.core.data_source.Game).

Classes that inherit from [`DataSource`](#ratingsystems.core.data_source.DataSource) must also implement a [`Meta`](#ratingsystems.core.data_source.DataSource.Meta) class. See [`Meta`](#ratingsystems.core.data_source.DataSource.Meta) class below for more details.

Classes that inherit from [`DataSource`](#ratingsystems.core.data_source.DataSource) can accept any options to __init__, but they must have a default value, and it must accept a year (int) as its first argument.

<a id="ratingsystems.core.data_source.DataSource.fetch"></a>

#### fetch

```python
@abstractmethod
def fetch() -> list[Game]
```

Method to fetch game data.

**Returns**:

  list of [`Game`](#ratingsystems.core.data_source.Game) objects

<a id="ratingsystems.core.data_source.DataSource.save"></a>

#### save

```python
def save(games: list[Game])
```

Save game data to local disk.

**Arguments**:

- `games` _list[[`Game`](#ratingsystems.core.data_source.Game)]_ - list of games

<a id="ratingsystems.core.data_source.DataSource.load"></a>

#### load

```python
def load(incomplete: bool = True) -> list[Game]
```

Load game data from local disk.

**Returns**:

  list of [`Game`](#ratingsystems.core.data_source.Game)

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

<a id="ratingsystems.core.data_source.DataSource.Meta"></a>

## Meta

```python
class Meta()
```

<a id="ratingsystems.core.data_source.DataSource.Meta.name"></a>

#### name

<a id="ratingsystems.core.data_source.DataSource.Meta.stats_class"></a>

#### stats\_class

<a id="ratingsystems.core.model.bracket"></a>

# ratingsystems.core.model.bracket

<a id="ratingsystems.core.model.bracket.dataclass"></a>

## dataclass

<a id="ratingsystems.core.model.bracket.Any"></a>

## Any

<a id="ratingsystems.core.model.bracket.Callable"></a>

## Callable

<a id="ratingsystems.core.model.bracket.Dict"></a>

## Dict

<a id="ratingsystems.core.model.bracket.List"></a>

## List

<a id="ratingsystems.core.model.bracket.Optional"></a>

## Optional

<a id="ratingsystems.core.model.bracket.Tuple"></a>

## Tuple

<a id="ratingsystems.core.model.bracket.Bracket"></a>

## Bracket

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

<a id="ratingsystems.core.model.game"></a>

# ratingsystems.core.model.game

<a id="ratingsystems.core.model.game.dataclass"></a>

## dataclass

<a id="ratingsystems.core.model.game.field"></a>

## field

<a id="ratingsystems.core.model.game.InitVar"></a>

## InitVar

<a id="ratingsystems.core.model.game.datetime"></a>

## datetime

<a id="ratingsystems.core.model.game.Any"></a>

## Any

<a id="ratingsystems.core.model.game.Optional"></a>

## Optional

<a id="ratingsystems.core.model.game.Type"></a>

## Type

<a id="ratingsystems.core.model.game.GameStats"></a>

## GameStats

```python
@dataclass
class GameStats()
```

<a id="ratingsystems.core.model.game.GameStats.points"></a>

#### points

<a id="ratingsystems.core.model.game.GameStats.period_points"></a>

#### period\_points

<a id="ratingsystems.core.model.game.Game"></a>

## Game

```python
@dataclass
class Game()
```

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

<a id="ratingsystems.core.model.prediction"></a>

# ratingsystems.core.model.prediction

<a id="ratingsystems.core.model.prediction.Optional"></a>

## Optional

<a id="ratingsystems.core.model.prediction.Prediction"></a>

## Prediction

```python
class Prediction()
```

<a id="ratingsystems.core.model.rating"></a>

# ratingsystems.core.model.rating

<a id="ratingsystems.core.model.rating.functools"></a>

## functools

<a id="ratingsystems.core.model.rating.math"></a>

## math

<a id="ratingsystems.core.model.rating.np"></a>

## np

<a id="ratingsystems.core.model.rating.ABC"></a>

## ABC

<a id="ratingsystems.core.model.rating.abstractmethod"></a>

## abstractmethod

<a id="ratingsystems.core.model.rating.Iterable"></a>

## Iterable

<a id="ratingsystems.core.model.rating.Enum"></a>

## Enum

<a id="ratingsystems.core.model.rating.Number"></a>

## Number

<a id="ratingsystems.core.model.rating.stdev"></a>

## stdev

<a id="ratingsystems.core.model.rating.Any"></a>

## Any

<a id="ratingsystems.core.model.rating.Optional"></a>

## Optional

<a id="ratingsystems.core.model.rating.Self"></a>

## Self

<a id="ratingsystems.core.model.rating.Union"></a>

## Union

<a id="ratingsystems.core.model.rating.Tuple"></a>

## Tuple

<a id="ratingsystems.core.model.rating.Type"></a>

## Type

<a id="ratingsystems.core.model.rating.Prediction"></a>

## Prediction

<a id="ratingsystems.core.model.rating.TeamRating"></a>

## TeamRating

<a id="ratingsystems.core.model.rating.Stat"></a>

## Stat

<a id="ratingsystems.core.model.rating.Rating"></a>

## Rating

```python
class Rating()
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

<a id="ratingsystems.core.model.rating.Rating.rank"></a>

#### rank

```python
@staticmethod
def rank(rating: Self, reverse: bool = False) -> list[Tuple[str, Stat]]
```

<a id="ratingsystems.core.model.stat"></a>

# ratingsystems.core.model.stat

<a id="ratingsystems.core.model.stat.Number"></a>

## Number

<a id="ratingsystems.core.model.stat.Any"></a>

## Any

<a id="ratingsystems.core.model.stat.Self"></a>

## Self

<a id="ratingsystems.core.model.stat.Stat"></a>

## Stat

```python
class Stat()
```

<a id="ratingsystems.core.model.stat.Stat.formatted"></a>

#### formatted

```python
def formatted(precision: int = 1) -> str
```

<a id="ratingsystems.core.model.team_rating"></a>

# ratingsystems.core.model.team\_rating

<a id="ratingsystems.core.model.team_rating.Iterable"></a>

## Iterable

<a id="ratingsystems.core.model.team_rating.Optional"></a>

## Optional

<a id="ratingsystems.core.model.team_rating.Self"></a>

## Self

<a id="ratingsystems.core.model.team_rating.Stat"></a>

## Stat

<a id="ratingsystems.core.model.team_rating.TeamRating"></a>

## TeamRating

```python
class TeamRating()
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

<a id="ratingsystems.core.model"></a>

# ratingsystems.core.model

<a id="ratingsystems.core.model.Bracket"></a>

## Bracket

<a id="ratingsystems.core.model.Game"></a>

## Game

<a id="ratingsystems.core.model.GameStats"></a>

## GameStats

<a id="ratingsystems.core.model.Prediction"></a>

## Prediction

<a id="ratingsystems.core.model.Rating"></a>

## Rating

<a id="ratingsystems.core.model.Stat"></a>

## Stat

<a id="ratingsystems.core.model.TeamRating"></a>

## TeamRating

<a id="ratingsystems.core.predictor"></a>

# ratingsystems.core.predictor

Defines a predictor, which can be used to predict a matchup between two teams.

A predictor can be used by calling the [`Predictor.predict`](#ratingsystems.core.predictor.Predictor.predict) function with a team and an opponent. This will return a [`Prediction`](#ratingsystems.core.predictor.Prediction) of the matchup.

This is also exposed via the CLI command `predict`, which can be called like this:
```bash
ratingsystems predict TEAM OPPONENT --data <datasource> --rating <ratingsystem> --predictor <predictor>
```

<a id="ratingsystems.core.predictor.st"></a>

## st

<a id="ratingsystems.core.predictor.ABC"></a>

## ABC

<a id="ratingsystems.core.predictor.abstractmethod"></a>

## abstractmethod

<a id="ratingsystems.core.predictor.signature"></a>

## signature

<a id="ratingsystems.core.predictor.Optional"></a>

## Optional

<a id="ratingsystems.core.predictor.click"></a>

## click

<a id="ratingsystems.core.predictor.ParameterSource"></a>

## ParameterSource

<a id="ratingsystems.core.predictor.Prediction"></a>

## Prediction

<a id="ratingsystems.core.predictor.Rating"></a>

## Rating

<a id="ratingsystems.core.predictor.Predictor"></a>

## Predictor

```python
class Predictor(ABC)
```

Abstract class used to create a predictor.

Classes that inherit from [`Predictor`](#ratingsystems.core.predictor.Predictor) must implement a [`predict`](#ratingsystems.core.predictor.Predictor.predict) method which takes as input a team and an opponent and returns a [`Prediction`](#ratingsystems.core.predictor.Prediction) object.

Classes that inherit from [`Predictor`](#ratingsystems.core.predictor.Predictor) must also implement a [`Meta`](#ratingsystems.core.predictor.Predictor.Meta) class. See [`Meta`](#ratingsystems.core.predictor.Predictor.Meta) class below for more details.

Classes that inherit from [`Predictor`](#ratingsystems.core.predictor.Predictor) can accept any options to __init__, but they must have a default value, and it must accept a [`Rating`](#ratingsystems.core.predictor.Rating) as its first argument.

<a id="ratingsystems.core.predictor.Predictor.predict"></a>

#### predict

```python
@abstractmethod
def predict(team: str, opponent: str) -> Prediction
```

Method to predict a matchup of two teams.

**Arguments**:

- `team` _str_ - first team of the matchup
- `opponent` _str_ - second team of the matchup
  

**Returns**:

  [`Prediction`](#ratingsystems.core.predictor.Prediction) object with prediction for the matchup

<a id="ratingsystems.core.predictor.Predictor.Meta"></a>

## Meta

```python
class Meta()
```

<a id="ratingsystems.core.predictor.Predictor.Meta.name"></a>

#### name

<a id="ratingsystems.core.predictor.AggregatePredictor"></a>

## AggregatePredictor

```python
class AggregatePredictor()
```

<a id="ratingsystems.core.predictor.AggregatePredictor.predict"></a>

#### predict

```python
def predict(team: str, opponent: str) -> Prediction
```

<a id="ratingsystems.core.predictor.RatingDifferencePredictor"></a>

## RatingDifferencePredictor

```python
class RatingDifferencePredictor(Predictor)
```

<a id="ratingsystems.core.predictor.RatingDifferencePredictor.predict"></a>

#### predict

```python
def predict(team: str, opponent: str) -> Prediction
```

<a id="ratingsystems.core.rating_system"></a>

# ratingsystems.core.rating\_system

Defines a rating system, which can be used to create a rating of teams.

A rating system can be used by calling the [`RatingSystem.rate`](#ratingsystems.core.rating_system.RatingSystem.rate) function with a list of [`Game`](#ratingsystems.core.rating_system.Game). This will return a [`Rating`](#ratingsystems.core.rating_system.Rating) of the teams.

This is also exposed via the CLI command `rate`, which can be called like this:
```bash
ratingsystems rate --data <datasource> --rating <ratingsystem>
```

<a id="ratingsystems.core.rating_system.ABC"></a>

## ABC

<a id="ratingsystems.core.rating_system.abstractmethod"></a>

## abstractmethod

<a id="ratingsystems.core.rating_system.signature"></a>

## signature

<a id="ratingsystems.core.rating_system.click"></a>

## click

<a id="ratingsystems.core.rating_system.ParameterSource"></a>

## ParameterSource

<a id="ratingsystems.core.rating_system.Game"></a>

## Game

<a id="ratingsystems.core.rating_system.Rating"></a>

## Rating

<a id="ratingsystems.core.rating_system.RatingSystem"></a>

## RatingSystem

```python
class RatingSystem(ABC)
```

Abstract class used to create a rating system.

Classes that inherit from [`RatingSystem`](#ratingsystems.core.rating_system.RatingSystem) must implement a [`rate`](#ratingsystems.core.rating_system.RatingSystem.rate) method which takes as input a list of [`Game`](#ratingsystems.core.rating_system.Game) objects and returns a [`Rating`](#ratingsystems.core.rating_system.Rating) object.

Classes that inherit from [`RatingSystem`](#ratingsystems.core.rating_system.RatingSystem) must also implement a [`Meta`](#ratingsystems.core.rating_system.RatingSystem.Meta) class. See [`Meta`](#ratingsystems.core.rating_system.RatingSystem.Meta) class below for more details.

Classes that inherit from [`RatingSystem`](#ratingsystems.core.rating_system.RatingSystem) can accept any options to __init__, but they must have a default value.

<a id="ratingsystems.core.rating_system.RatingSystem.rate"></a>

#### rate

```python
@abstractmethod
def rate(games: list[Game]) -> Rating
```

Method to create a rating based on game data.

**Arguments**:

- `games` _list[[`Game`](#ratingsystems.core.rating_system.Game)]_ - list of games
  

**Returns**:

  [`Rating`](#ratingsystems.core.rating_system.Rating) object with a rating for each team found in the game data

<a id="ratingsystems.core.rating_system.RatingSystem.Meta"></a>

## Meta

```python
class Meta()
```

Meta class for a rating system. Any class that inherits from RatingSystem must override this Meta class and set the name field.

<a id="ratingsystems.core.rating_system.RatingSystem.Meta.name"></a>

#### name

<a id="ratingsystems.core.util.file"></a>

# ratingsystems.core.util.file

<a id="ratingsystems.core.util.file.os"></a>

## os

<a id="ratingsystems.core.util.file.config_path"></a>

#### config\_path

<a id="ratingsystems.core.util.math"></a>

# ratingsystems.core.util.math

<a id="ratingsystems.core.util.math.np"></a>

## np

<a id="ratingsystems.core.util.math.LinearRegression"></a>

## LinearRegression

<a id="ratingsystems.core.util.math.LogisticRegression"></a>

## LogisticRegression

<a id="ratingsystems.core.util.math.PolynomialFeatures"></a>

## PolynomialFeatures

<a id="ratingsystems.core.util.math.Optional"></a>

## Optional

<a id="ratingsystems.core.util.math.Union"></a>

## Union

<a id="ratingsystems.core.util.math.Rating"></a>

## Rating

<a id="ratingsystems.core.util.math.Stat"></a>

## Stat

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

<a id="ratingsystems.core.util.text"></a>

# ratingsystems.core.util.text

<a id="ratingsystems.core.util.text.math"></a>

## math

<a id="ratingsystems.core.util.text.Any"></a>

## Any

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

<a id="ratingsystems.core.util"></a>

# ratingsystems.core.util

<a id="ratingsystems.core.util.config_path"></a>

## config\_path

<a id="ratingsystems.core.util.linear_regression"></a>

## linear\_regression

<a id="ratingsystems.core.util.linear_regression_to_points"></a>

## linear\_regression\_to\_points

<a id="ratingsystems.core.util.logistic_regression"></a>

## logistic\_regression

<a id="ratingsystems.core.util.center"></a>

## center

<a id="ratingsystems.core.util.ljustify"></a>

## ljustify

<a id="ratingsystems.core.util.rjustify"></a>

## rjustify

<a id="ratingsystems.core"></a>

# ratingsystems.core

<a id="ratingsystems.core.DataSource"></a>

## DataSource

<a id="ratingsystems.core.Bracket"></a>

## Bracket

<a id="ratingsystems.core.Game"></a>

## Game

<a id="ratingsystems.core.GameStats"></a>

## GameStats

<a id="ratingsystems.core.Prediction"></a>

## Prediction

<a id="ratingsystems.core.Rating"></a>

## Rating

<a id="ratingsystems.core.Stat"></a>

## Stat

<a id="ratingsystems.core.TeamRating"></a>

## TeamRating

<a id="ratingsystems.core.AggregatePredictor"></a>

## AggregatePredictor

<a id="ratingsystems.core.Predictor"></a>

## Predictor

<a id="ratingsystems.core.RatingDifferencePredictor"></a>

## RatingDifferencePredictor

<a id="ratingsystems.core.RatingSystem"></a>

## RatingSystem

