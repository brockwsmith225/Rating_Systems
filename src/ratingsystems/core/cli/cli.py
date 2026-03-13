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

from ratingsystems.core import DataSource, Predictor, RatingDifferencePredictor, RatingSystem
from ratingsystems.core.cli.helpers import KeyValuePair, SelectChoice, combine_key_value_pairs, filter_options
from ratingsystems.core.model import Rating
from ratingsystems.core.util import center, ljustify, rjustify


# Common options
year = click.option("--year", "-y", type=int, default=datetime.now().year, help="Year of data to use")
datasource = click.option("--data", "-d", "datasource", type=SelectChoice({}, case_sensitive=False), help="Select a data source from those you've installed")
ratingsystem = click.option("--rating", "-r", "ratingsystem", type=SelectChoice({}, case_sensitive=False), help="Select a rating system from those you've installed")
predictor = click.option("--predictor", "-p", "predictor", type=SelectChoice({RatingDifferencePredictor.name: RatingDifferencePredictor}, case_sensitive=False), default=RatingDifferencePredictor.name, help="Select a predictor from those you've installed")
options = click.option("--opt", "-o", "options", multiple=True, type=KeyValuePair(), default={}, callback=combine_key_value_pairs, help="Set an option to be passed to any plugin that accepts it, can be set multiple times, see specific plugin documentation for what options are available")


def load_cli_plugins():
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
    context,
    year: int = datetime.now().year,
    datasource: Optional[DataSource] = None,
    ratingsystem: Optional[RatingSystem] = None,
    predictor: Optional[Predictor] = None,
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
    context,
    year: int = datetime.now().year,
    datasource: Optional[DataSource] = None,
    ratingsystem: Optional[RatingSystem] = None,
    predictor: Optional[Predictor] = None,
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
            click.echo(f"ratingsystem={ratingsystem.name}")
        if predictor is not None:
            click.echo(f"predictor={predictor.name}")
        if len(options) > 0:
            click.echo(f"options={options}")


def set_defaults(context, new_parameters: Optional[dict[str, Any]] = None) -> dict[str, Any]:
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
                parameters[param] = context.default_map.get(param, ()) + value
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
@click.pass_context
def fetch(
    context,
    year: int = datetime.now().year,
    datasource: Optional[DataSource] = None,
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
@click.option("--ranks/--no-ranks", type=bool, is_flag=True, default=False, help="Print ranks for each rating")
@click.option("--hidden/--no-hidden", type=bool, is_flag=True, default=False, help="Include hidden ratings in output")
@click.pass_context
def rate(
    context,
    year: int = datetime.now().year,
    datasource: Optional[DataSource] = None,
    ratingsystem: Optional[RatingSystem] = None,
    pretty: bool = False,
    ranks: bool = False,
    hidden: bool = False,
    options: dict[str, Any] = {},
):
    """
    Used to create a rating.
    """
    if datasource is None:
        click.echo("Input Error: must specify a data source (-d, --data)")
        context.exit(1)

    if ratingsystem is None:
        click.echo("Input Error: must specify a rating system (-r, --rating)")
        context.exit(1)

    data = datasource(year)

    # Try to load data
    try:
        games = data.load(incomplete=False)
    except Exception as e:
        click.echo(f"Error in loading data for {datasource.name} {year}: {e}")
        context.exit(1)

    rs = ratingsystem(**filter_options(options, ratingsystem))

    try:
        rating = rs.rate(games)
    except Exception as e:
        click.echo(f"Error in creating rating for {ratingsystem.name} {year}: {e}")
        context.exit(1)

    # Store rating for shell mode
    context.obj["ratings"][rs.name] = rating

    # TODO: add rankings

    if pretty:
        click.echo(f"{rjustify('RANK', 4)} | {ljustify('TEAM', 30)} | {center('RECORD', 7)} | {' | '.join([center(r.name.upper(), 10) for r in rating.ratings(hidden=hidden)])}")
    else:
        click.echo(f"RANK,TEAM,RECORD,{','.join([r.name.upper() for r in rating.ratings(hidden=hidden)])}")

    rank = 1
    for team in Rating.rank(rating):
        if pretty:
            click.echo(f"{rjustify(rank, 4)} | {ljustify(team.name, 30)} | {rjustify(team.wins, 3)}-{ljustify(team.losses, 3)} | {' | '.join([center(rating.formatted(), 10) for rating in team.ratings(hidden=hidden)])}")
        else:
            click.echo(f"{rank},{team.name},{team.wins}-{team.losses},{','.join([str(rating.value) for rating in team.ratings(hidden=hidden)])}")
        rank += 1


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
    context,
    team: str,
    opponent: str,
    year: int = datetime.now().year,
    datasource: Optional[DataSource] = None,
    ratingsystem: Optional[RatingSystem] = None,
    predictor: Optional[Predictor] = None,
    options: dict[str, Any] = {},
):
    """
    Used to predict a matchup between TEAM and OPPONENT.

    \b
      TEAM first team in the matchup
      OPPONENT second team in the matchup
    """
    if datasource is None:
        click.echo("Input Error: must specify a data source (-d, --data)")
        context.exit(1)

    if ratingsystem is None:
        click.echo("Input Error: must specify a rating system (-r, --rating)")
        context.exit(1)

    data = datasource(year)

    # Try to load data
    try:
        games = data.load(incomplete=False)
    except Exception as e:
        click.echo(f"Error in loading data for {datasource.name} {year}: {e}")
        context.exit(1)

    if ratingsystem.name in context.obj["ratings"]:
        # If in shell mode and we've already made a rating with this rating system, use it
        rating = context.obj["ratings"][ratingsystem.name]
    else:
        rs = ratingsystem(**filter_options(options, ratingsystem))

        try:
            rating = rs.rate(games)
        except Exception as e:
            click.echo(f"Error in creating rating for {ratingsystem.name} {datasource.name} {year}: {e}")
            context.exit(1)

        # Store rating for shell mode
        context.obj["ratings"][rs.name] = rating

    p = predictor(rating, **filter_options(options, ratingsystem))

    # Try to predict a matchup between team and opponent
    try:
        prediction = p.predict(team, opponent)
    except Exception as e:
        click.echo(f"Error in creating prediction for {predictor.name} {ratingsystem.name} {datasource.name} {year}: {e}")
        context.exit(1)

    click.echo(prediction)


load_cli_plugins()
