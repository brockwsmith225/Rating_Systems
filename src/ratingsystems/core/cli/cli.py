import inspect
import pkgutil
from importlib.metadata import entry_points
from abc import ABC, abstractmethod
from datetime import datetime
from inspect import isclass, signature
from typing import Any, Optional

import click
from click_shell import shell
from click.core import ParameterSource

from ratingsystems.core import AggregatePredictor, DataSource, Predictor, RatingDifferencePredictor, RatingSystem
from ratingsystems.core.cli.helpers import KeyValuePair, SelectChoice, combine_key_value_pairs, filter_options
from ratingsystems.core.model import Rating
from ratingsystems.core.util import center, ljustify, rjustify


# Common options
year = click.option("--year", "-y", type=int, default=datetime.now().year, help="Year of data to use")
datasource = click.option("--data", "-d", "datasource", type=SelectChoice({}, case_sensitive=False), help="Select a data source from those you've installed")
ratingsystem = click.option("--rating", "-r", "ratingsystem", type=SelectChoice({}, case_sensitive=False), multiple=True, default=(), help="Select a rating system from those you've installed, can be set multiple times to combine rating systems")
predictor = click.option("--predictor", "-p", "predictor", type=SelectChoice({RatingDifferencePredictor.name: RatingDifferencePredictor}, case_sensitive=False), multiple=True, default=(RatingDifferencePredictor.name,), help="Select a predictor from those you've installed, can be set multiple times to aggregate predictors")
options = click.option("--opt", "-o", "options", multiple=True, type=KeyValuePair(), default={}, callback=combine_key_value_pairs, help="Set an option to be passed to any plugin that accepts it, can be set multiple times, see specific plugin documentation for what options are available")


def _load_cli_plugins():
    # TODO: handle without needing entry points defined?
    # import ratingsystems
    # for m in pkgutil.iter_modules(ratingsystems.__path__):
    #     print(m)

    for entry_point in entry_points(group="ratingsystems"):
        plugin = entry_point.load()
        for type in [DataSource, RatingSystem, Predictor]:
            if not issubclass(plugin, type):
                continue
            for param in cli.params:
                if param.name == type.__name__.lower() and isinstance(param.type, click.Choice):
                    param.type.choices[plugin.name] = plugin


@shell(prompt="ratingsystems > ", intro="Starting ratingsystems cli...", context_settings={'show_default': True})
@year
@datasource
@ratingsystem
@predictor
@options
@click.pass_context
def cli(
    context: click.Context,
    year: int = datetime.now().year,
    datasource: Optional[Type[DataSource]] = None,
    ratingsystem: Tuple[Type[RatingSystem]] = (),
    predictor: Tuple[Type[Predictor]] = (),
    options: dict[str, Any] = {},
):
    """
    CLI for interacting with rating systems. Use without a subcommand to start a shell.
    """
    context.ensure_object(dict)
    context.obj = {
        "ratings": {},
    }
    context.default_map = {}
    set_defaults(context)


@cli.command()
@year
@datasource
@ratingsystem
@predictor
@options
@click.pass_context
def config(
    context: click.Context,
    year: int = datetime.now().year,
    datasource: Optional[DataSource] = None,
    ratingsystem: Tuple[Type[RatingSystem]] = (),
    predictor: Tuple[Type[Predictor]] = (),
    options: dict[str, Any] = {},
):
    """
    Used to set config values or see current config.
    """
    set_defaults(context)

    if all([ps in [ParameterSource.DEFAULT, ParameterSource.DEFAULT_MAP] for ps in context._parameter_source.values()]):
        if year is not None:
            click.echo(f"year={year}")
        if datasource is not None:
            click.echo(f"datasource={datasource.name}")
        if ratingsystem is not None:
            click.echo(f"ratingsystem={[r.name for r in ratingsystem]}")
        if predictor is not None:
            click.echo(f"predictor={predictor.name}")
        if len(options) > 0:
            click.echo(f"options={options}")


def set_defaults(context: click.Context, new_parameters: Optional[dict[str, Any]] = None) -> dict[str, Any]:
    if context.parent is not None:
        context.default_map = set_defaults(context.parent, context.params)
    else:
        if new_parameters is None:
            new_parameters = context.params

        parameters = {}
        for param, value in new_parameters.items():
            if isclass(value):
                parameters[param] = value.name
            elif isinstance(value, tuple):
                parameters[param] = tuple([v.name if isclass(v) else v for v in value])
            elif isinstance(value, dict):
                parameters[param] = {k: v for k, v in {**context.default_map.get(param, {}), **value}.items() if v is not None}
            else:
                parameters[param] = value

        # Assign parameters as the default map for the root command and all sub commands
        context.default_map = parameters.copy()
        for command in context.command.commands:
            # TODO: get this to work for a subcommand's subcommand
            context.default_map[command] = parameters.copy()

    return context.default_map


@cli.command()
@year
@datasource
@click.option("--bracket", type=bool, is_flag=True, default=False, help="Fetch bracket instead of game data")
@click.pass_context
def fetch(
    context: click.Context,
    year: int = datetime.now().year,
    datasource: Optional[Type[DataSource]] = None,
    bracket: bool = False,
):
    """
    Used to fetch data.
    """
    if datasource is None:
        click.echo("Input Error: must specify a data source (-d, --data)")
        context.exit(1)

    data = datasource(year)

    if data.auth_token is None:
        click.echo(f"No auth token found for data source {datasource.name}")
        data.auth_token = click.prompt("Auth token", type=str, hide_input=True)

    if bracket:
        try:
            click.echo(f"Fetching bracket for {datasource.name} {year} ...")
            bracket = data.fetch_bracket()
            click.echo("Fetched bracket")
        except Exception as e:
            click.echo(f"Error in fetching bracket for {datasource.name} {year}: {e}")
            context.exit(1)

        try:
            click.echo("Saving bracket ...")
            data.save_bracket(bracket)
            click.echo("Saved bracket")
        except Exception as e:
            click.echo(f"Error in saving bracket for {datasource.name} {year}: {e}")
            context.exit(1)

    else:
        try:
            click.echo(f"Fetching data for {datasource.name} {year} ...")
            games = data.fetch()
            click.echo(f"Fetched data: {len(games)} games")
        except Exception as e:
            click.echo(f"Error in fetching data for {datasource.name} {year}: {e}")
            context.exit(1)

        try:
            click.echo("Saving data ...")
            data.save(games)
            click.echo("Saved data")
        except Exception as e:
            click.echo(f"Error in saving data for {datasource.name} {year}: {e}")
            context.exit(1)


@cli.command()
@year
@datasource
@ratingsystem
@options
@click.option("--pretty/--no-pretty", type=bool, is_flag=True, default=False, help="Pretty print rating")
@click.option("--ranks/--no-ranks", "include_ranks", type=bool, is_flag=True, default=False, help="Print ranks for each rating")
@click.option("--hidden/--no-hidden", type=bool, is_flag=True, default=False, help="Include hidden ratings in output")
@click.pass_context
def rate(
    context: click.Context,
    year: int = datetime.now().year,
    datasource: Optional[Type[DataSource]] = None,
    ratingsystem: Tuple[Type[RatingSystem]] = (),
    pretty: bool = False,
    include_ranks: bool = False,
    hidden: bool = False,
    options: dict[str, Any] = {},
):
    """
    Used to create a rating.
    """
    games = _load_games(context, datasource, year)

    rating = _create_rating(context, ratingsystem, options, games)

    ranking = Rating.rank(rating)

    ranks = {}
    if include_ranks:
        for team in rating.teams():
            ranks[team] = [r.get_rank(team) for r in rating.ratings(hidden=hidden)]
    else:
        for team in rating.teams():
            ranks[team] = [rating.get_rank(team)]

    if pretty:
        click.echo(f"| {rjustify('RANK', 4)} | ", nl=False)
        click.echo(f"{ljustify('TEAM', 30)} | ", nl=False)
        click.echo(f"{center('RECORD', 7)} | ", nl=False)
        click.echo(f"{center('CONFERENCE', 15)} | ", nl=False)
        for r in rating.ratings(hidden=hidden):
            if include_ranks:
                click.echo(f"{center(r.name.upper(), 13)} | ", nl=False)
            else:
                click.echo(f"{center(r.name.upper(), 10)} | ", nl=False)
        click.echo()
        click.echo(f"|{'-' * 6}|", nl=False)
        click.echo(f"{'-' * 32}|", nl=False)
        click.echo(f"{'-' * 9}|", nl=False)
        click.echo(f"{'-' * 17}|", nl=False)
        for r in rating.ratings(hidden=hidden):
            if include_ranks:
                click.echo(f"{'-' * 15}|", nl=False)
            else:
                click.echo(f"{'-' * 12}|", nl=False)
        click.echo()
    else:
        click.echo("RANK,", nl=False)
        click.echo("TEAM,", nl=False)
        click.echo("RECORD,", nl=False)
        click.echo("CONFERENCE,", nl=False)
        for r in rating.ratings(hidden=hidden):
            if include_ranks:
                click.echo(f"{r.name.upper()},", nl=False)
            else:
                click.echo(f"{r.name.upper()},", nl=False)
        click.echo()

    for team in ranking:
        if pretty:
            click.echo(f"| {rjustify(ranks[team.name][0], 4)} | ", nl=False)
            click.echo(f"{ljustify(team.name, 30)} | ", nl=False)
            click.echo(f"{rjustify(team.wins, 3)}-{ljustify(team.losses, 3)} | ", nl=False)
            click.echo(f"{ljustify(team.conference, 15)} | ", nl=False)
            if include_ranks:
                for r, rank in zip(team.ratings(hidden=hidden), ranks[team.name]):
                    click.echo(f"{rjustify(r.formatted(), 6)} {ljustify('(' + str(rank) + ')', 6)} | ", nl=False)
            else:
                for r in team.ratings(hidden=hidden):
                    click.echo(f"{center(r.formatted(), 10)} | ", nl=False)
            click.echo()
        else:
            click.echo(f"{ranks[team.name][0]},", nl=False)
            click.echo(f"{team.name},", nl=False)
            click.echo(f"{team.wins}-{team.losses},", nl=False)
            click.echo(f"{team.conference},", nl=False)
            if include_ranks:
                for r, rank in zip(team.ratings(hidden=hidden), ranks[team.name]):
                    click.echo(f"{r.value},{rank},", nl=False)
            else:
                for r in team.ratings(hidden=hidden):
                    click.echo(f"{r.value},", nl=False)
            click.echo()


@cli.group(invoke_without_command=True)
@click.argument("team", type=str)
@click.argument("opponent", type=str)
@year
@datasource
@ratingsystem
@predictor
@options
@click.pass_context
def predict(
    context: click.Context,
    team: str,
    opponent: str,
    year: int = datetime.now().year,
    datasource: Optional[Type[DataSource]] = None,
    ratingsystem: Tuple[Type[RatingSystem]] = (),
    predictor: Tuple[Type[Predictor]] = (),
    options: dict[str, Any] = {},
):
    """
    Used to predict a matchup between TEAM and OPPONENT.

    \b
      TEAM first team in the matchup
      OPPONENT second team in the matchup
    """
    games = _load_games(context, datasource, year)

    rating = _create_rating(context, ratingsystem, options, games, load_rating=True)

    pred = _create_predictor(context, predictor, options, rating)
    prediction = _create_prediction(context, pred, team, opponent)

    click.echo(prediction)


@cli.group(invoke_without_command=True)
@year
@datasource
@ratingsystem
@predictor
@options
@click.option("--display/--no-display", type=bool, is_flag=True, default=False, help="Display bracket with picks instead of a table of odds")
@click.option("--pretty/--no-pretty", type=bool, is_flag=True, default=False, help="Pretty print bracket odds")
@click.pass_context
def bracket(
    context: click.Context,
    year: int = datetime.now().year,
    datasource: Optional[Type[DataSource]] = None,
    ratingsystem: Tuple[Type[RatingSystem]] = (),
    predictor: Tuple[Type[Predictor]] = (),
    options: dict[str, Any] = {},
    display: bool = False,
    pretty: bool = False,
):
    """
    Used to produce odds for the results of a bracket.
    """
    games = _load_games(context, datasource, year)
    bracket = _load_bracket(context, datasource, year)

    rating = _create_rating(context, ratingsystem, options, games, load_rating=True)

    p = _create_predictor(context, predictor, options, rating)

    # Try to evaluate the bracket
    # try:
    bracket.evaluate(p)
    # except Exception as e:
    #     click.echo(f"Error in evaluating the bracket: {e}")
    #     context.exit(1)

    if display:
        click.echo(bracket)
    else:
        for team, value in bracket.full_odds.items():
            region, seed, odds = value
            if pretty:
                click.echo(f"{rjustify(seed, 4)} | {ljustify(team, 30)} | {center(rating.get(team).formatted(), 10)} | {center(region, 10)} | {' | '.join([center(str(round(o * 100, 1)) + '%', 10) for o in odds])}")
            else:
                click.echo(f"{seed},{team},{rating.get_value(team)},{region},{','.join([str(o) for o in odds])}")


def _load_games(context: click.Context, datasource: Type[DataSource], year: int) -> list[Game]:
    if datasource is None:
        click.echo("Input Error: must specify a data source (-d, --data)")
        context.exit(1)

    data = datasource(year)

    # Try to load data
    try:
        games = data.load(incomplete=False)
    except Exception as e:
        click.echo(f"Error in loading data for {datasource.name} {year}: {e}")
        context.exit(1)

    return games


def _load_bracket(context: click.Context, datasource: Type[DataSource], year: int) -> list[Game]:
    if datasource is None:
        click.echo("Input Error: must specify a data source (-d, --data)")
        context.exit(1)

    data = datasource(year)

    # Try to load bracket
    try:
        bracket = data.load_bracket()
    except Exception as e:
        click.echo(f"Error in loading bracket for {datasource.name} {year}: {e}")
        context.exit(1)

    return bracket


def _create_rating(context: click.Context, ratingsystems: Tuple[Type[RatingSystem]], options: dict[str, Any], games: list[Game], save_rating: bool = True, load_rating: bool = False) -> Rating:
    if len(ratingsystems) == 0:
        click.echo("Input Error: must specify a rating system (-r, --rating)")
        context.exit(1)

    ratings = []

    for ratingsystem in ratingsystems:
        if load_rating and ratingsystem.name in context.obj["ratings"]:
            # If in shell mode and we've already made a rating with this rating system, use it
            ratings.append(context.obj["ratings"][ratingsystem.name])

        rs = ratingsystem(**filter_options(options, ratingsystem))

        # try:
        ratings.append(rs.rate(games))
        # except Exception as e:
        #     click.echo(f"Error in creating rating for {ratingsystem.name}: {e}")
        #     context.exit(1)

        if save_rating:
            # Store rating for shell mode
            context.obj["ratings"][rs.name] = ratings[-1]

    if len(ratings) == 1:
        return ratings[0]
    return (sum(ratings) / len(ratings)) % "aggregate"


def _create_predictor(context: click.Context, predictors: Tuple[Type[Predictor]], options: dict[str, Any], rating: Rating) -> Prediction:
    if len(predictors) == 0:
        click.echo("Input Error: must specify a predictor (-p, --predictor)")
        context.exit(1)

    preds = []

    for predictor in predictors:
        preds.append(predictor(rating, **filter_options(options, predictor)))

    predictor = AggregatePredictor(*preds)

    return predictor


def _create_prediction(context: click.Context, predictor: Predictor, team: str, opponent: str) -> Prediction:
    # Try to predict a matchup between team and opponent
    try:
        prediction = predictor.predict(team, opponent)
    except Exception as e:
        click.echo(f"Error in predicting {team} vs {opponent} for {predictor.name}: {e}")
        context.exit(1)

    return prediction


_load_cli_plugins()
