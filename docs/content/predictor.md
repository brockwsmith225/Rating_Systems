<a id="ratingsystems.core.predictor"></a>

# ratingsystems.core.predictor

<a id="ratingsystems.core.predictor.Predictor"></a>

## Predictor Objects

```python
class Predictor(ABC)
```

<a id="ratingsystems.core.predictor.Predictor.Meta"></a>

## Meta Objects

```python
class Meta()
```

<a id="ratingsystems.core.predictor.Predictor.Meta.name"></a>

#### name

<a id="ratingsystems.core.predictor.Predictor.predict"></a>

#### predict

```python
@abstractmethod
def predict(team: str, opponent: str) -> Prediction
```

