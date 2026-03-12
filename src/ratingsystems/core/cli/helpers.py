from inspect import signature
from typing import Any, Optional, Type

import click


def combine_key_value_pairs(ctx: click.Context, param: click.Parameter, value: tuple[dict[str, Any]]) -> dict[str, Any]:
    result = {}
    for d in value:
        result.update(d)
    return result


def filter_options(options: dict[str, Any], cls: Type):
    # Determine parameters for the selected rating system
    parameters = {}
    for param in signature(cls.__init__).parameters.values():
        if param.name == "self":
            continue
        type = param.annotation
        if hasattr(type, "_name") and type._name == "Optional":
            type = type.__args__[0]
        parameters[param.name] = type

    filtered_options = {}
    for param, type in parameters.items():
        if param in options:
            if type == bool:
                value = options[param].lower() == "true"
            else:
                value = type(options[param])
            filtered_options[param] = value

    return filtered_options


class SelectChoice(click.Choice):

    def __init__(self, choices: dict[str, Any], *args, **kwargs):
        super().__init__(choices, *args, **kwargs)
        self.choices = choices

    def convert(self, value: Optional[str] = None, param: Optional[click.Parameter] = None, ctx: Optional[click.Context] = None) -> Any:
        if value is None:
            return None

        value = super().convert(value, param, ctx)
        return self.choices.get(value)


class WeightedSelectChoice(SelectChoice):

    def convert(self, value: Optional[str] = None, param: Optional[click.Parameter] = None, ctx: Optional[click.Context] = None) -> Any:
        value, weight = KeyValuePair(delimiter=":", default=1).convert(value, param, ctx)

        return (super().convert(value, param, ctx), weight)


class KeyValuePair(click.ParamType):

    name = "KeyValuePair"

    def __init__(self, delimiter: str = "=", default: Optional[Any] = None):
        self.delimiter = delimiter
        self.default = default

    def convert(self, value: Optional[str] = None, param: Optional[click.Parameter] = None, ctx: Optional[click.Context] = None) -> dict[str, Any]:
        if value is None:
            return None

        pair = value.split(self.delimiter)
        if len(pair) == 2:
            key, value = pair
            if value == "":
                return {key: None}
            return {key: value}
        elif len(pair) == 1 and ctx is not None and pair[0] in ctx.default_map.get(param.name, {}):
            key = pair[0]
            return {key: ctx.default_map[param.name][key]}
        else:
            raise IOError(f"Invalid format for key-value pair '{value}'")

    def get_metavar(self, param: click.Parameter, ctx: Optional[click.Context] = None) -> str:
        return "KEY=VALUE"
