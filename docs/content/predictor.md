<a id="ratingsystems.core.predictor"></a>

# ratingsystems.core.predictor

Defines a predictor, which can be used to predict a matchup between two teams.

A predictor can be used by calling the [`Predictor.predict`](#ratingsystems.core.predictor.Predictor.predict) function with a team and an opponent. This will return a [`Prediction`](#ratingsystems.core.predictor.Prediction) of the matchup.

This is also exposed via the CLI command `predict`, which can be called like this:
```bash
ratingsystems predict --data <datasource> --rating <ratingsystem> --predictor <predictor> TEAM OPPONENT
```

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

<a id="ratingsystems.core.predictor.Predictor.Meta"></a>

## Meta

```python
class Meta()
```

<a id="ratingsystems.core.predictor.Predictor.Meta.name"></a>

#### name

