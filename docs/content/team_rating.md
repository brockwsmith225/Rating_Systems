<a id="ratingsystems.core.model.team_rating"></a>

# ratingsystems.core.model.team\_rating

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

