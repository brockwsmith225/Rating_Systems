<a id="ratingsystems.core.rating_system"></a>

# ratingsystems.core.rating\_system

<a id="ratingsystems.core.rating_system.RatingSystem"></a>

## RatingSystem Objects

```python
class RatingSystem(ABC)
```

Abstract class used to create a rating system.

Classes that inherit from RatingSystem must implement a rate method which takes as input a list of Game objects and returns a Rating object.

Classes that inherit from RatingSystem must also implement a [`Meta`](#ratingsystems.core.rating_system.RatingSystem.Meta) class. See Meta class below for more details.

Classes that inherit from RatingSystem can accept any options to __init__, but they must have a default value.

<a id="ratingsystems.core.rating_system.RatingSystem.Meta"></a>

## Meta Objects

```python
class Meta()
```

Meta class for a rating system. Any class that inherits from RatingSystem must override this Meta class and set the name field.

<a id="ratingsystems.core.rating_system.RatingSystem.Meta.name"></a>

#### name

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

