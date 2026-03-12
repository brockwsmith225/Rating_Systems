<a id="ratingsystems.core.model.rating"></a>

# ratingsystems.core.model.rating

<a id="ratingsystems.core.model.rating.Rating"></a>

## Rating Objects

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

