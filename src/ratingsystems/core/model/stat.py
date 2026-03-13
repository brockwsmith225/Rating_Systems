from numbers import Number
from typing import Any, Self


class Stat():
    """
    Class representing a rating stat. This provides a way to format a rating. 

    Classes can inherit from #Stat and override the #formatted method to format for different ratings.

    Parameters:
    - `value`_float_ - value of the stat

    #Stat objects can still be used with any arithmetic operator the same way as a number.

    #Stat objects can be formatted by calling the #formatted method or casting it to a string.
    """

    def __init__(self, value: float):
        self.value = value

    def formatted(self, precision: int = 1) -> str:
        """
        Formats the value of the #Stat.

        Args:
            precision (int): number of decimal places to round the value to (default: 1)

        Returns:
            string representation of the formatted value
        """
        return f"%.{precision}f" % round(self.value, precision)

    def __str__(self) -> str:
        return self.formatted()

    def __format__(self, format_spec) -> str:
        return self.formatted().__format__(format_spec)

    def __repr__(self) -> str:
        return self.formatted()

    def __add__(self, other: Any) -> Self:
        if isinstance(other, Stat):
            if type(self) == type(other):
                return type(self)(self.value + other.value)
            else:
                return Stat(self.value + other.value)
        elif isinstance(other, Number):
            return type(self)(self.value + other)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'Stat' and '{type(other)}'")

    def __radd__(self, other: Any) -> Self:
        if isinstance(other, Stat):
            if type(self) == type(other):
                return type(self)(other.value + self.value)
            else:
                return Stat(other.value + self.value)
        elif isinstance(other, Number):
            return type(self)(other + self.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: '{type(other)}' and 'Stat'")

    def __sub__(self, other: Any) -> Self:
        if isinstance(other, Stat):
            if type(self) == type(other):
                return type(self)(self.value - other.value)
            else:
                return Stat(self.value - other.value)
        elif isinstance(other, Number):
            return type(self)(self.value - other)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: 'Stat' and '{type(other)}'")

    def __rsub__(self, other: Any) -> Self:
        if isinstance(other, Stat):
            if type(self) == type(other):
                return type(self)(other.value - self.value)
            else:
                return Stat(other.value - self.value)
        elif isinstance(other, Number):
            return type(self)(other - self.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: '{type(other)}' and 'Stat'")

    def __mul__(self, other: Any) -> Self:
        if isinstance(other, Stat):
            if type(self) == type(other):
                return type(self)(self.value * other.value)
            else:
                return Stat(self.value * other.value)
        elif isinstance(other, Number):
            return type(self)(self.value * other)
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'Stat' and '{type(other)}'")

    def __rmul__(self, other: Any) -> Self:
        if isinstance(other, Stat):
            if type(self) == type(other):
                return type(self)(other.value * self.value)
            else:
                return Stat(other.value * self.value)
        elif isinstance(other, Number):
            return type(self)(other * self.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for *: '{type(other)}' and 'Stat'")

    def __truediv__(self, other: Any) -> Self:
        if isinstance(other, Stat):
            if type(self) == type(other):
                return type(self)(self.value / other.value)
            else:
                return Stat(self.value / other.value)
        elif isinstance(other, Number):
            return type(self)(self.value / other)
        else:
            raise TypeError(f"Unsupported operand type(s) for /: 'Stat' and '{type(other)}'")

    def __rtruediv__(self, other: Any) -> Self:
        if isinstance(other, Stat):
            if type(self) == type(other):
                return type(self)(other.value / self.value)
            else:
                return Stat(other.value / self.value)
        elif isinstance(other, Number):
            return type(self)(other / self.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for /: '{type(other)}' and 'Stat'")

    def __pow__(self, other: Any) -> Self:
        if isinstance(other, Stat):
            if type(self) == type(other):
                return type(self)(self.value ** other.value)
            else:
                return Stat(self.value ** other.value)
        elif isinstance(other, Number):
            return type(self)(self.value ** other)
        else:
            raise TypeError(f"Unsupported operand type(s) for **: 'Stat' and '{type(other)}'")

    def __rpow__(self, other: Any) -> Self:
        if isinstance(other, Stat):
            if type(self) == type(other):
                return type(self)(other.value ** self.value)
            else:
                return Stat(other.value ** self.value)
        elif isinstance(other, Number):
            return type(self)(other ** self.value)
        else:
            raise TypeError(f"Unsupported operand type(s) for **: '{type(other)}' and 'Stat'")

    def __abs__(self) -> Self:
        return type(self)(abs(self.value))
    