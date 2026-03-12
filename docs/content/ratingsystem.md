<a id="ratingsystems.core.rating_system"></a>

# ratingsystems.core.rating\_system

Defines a rating system, which can be used to create a rating of teams.

A rating system can be used by calling the [`RatingSystem.rate`](#ratingsystems.core.rating_system.RatingSystem.rate) function with a list of [`Game`](#ratingsystems.core.rating_system.Game). This will return a [`Rating`](#ratingsystems.core.rating_system.Rating) of the teams.

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

