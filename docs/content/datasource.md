<a id="ratingsystems.core.data_source"></a>

# ratingsystems.core.data\_source

<a id="ratingsystems.core.data_source.DataSource"></a>

## DataSource Objects

```python
class DataSource(ABC)
```

<a id="ratingsystems.core.data_source.DataSource.Meta"></a>

## Meta Objects

```python
class Meta()
```

<a id="ratingsystems.core.data_source.DataSource.Meta.name"></a>

#### name

<a id="ratingsystems.core.data_source.DataSource.Meta.stats_class"></a>

#### stats\_class

<a id="ratingsystems.core.data_source.DataSource.cli"></a>

#### cli

```python
def cli(context)
```

<a id="ratingsystems.core.data_source.DataSource.fetch"></a>

#### fetch

```python
@abstractmethod
def fetch() -> list[Game]
```

<a id="ratingsystems.core.data_source.DataSource.data_dir"></a>

#### data\_dir

```python
@property
def data_dir() -> str
```

<a id="ratingsystems.core.data_source.DataSource.data_path"></a>

#### data\_path

```python
@property
def data_path() -> str
```

<a id="ratingsystems.core.data_source.DataSource.auth_token"></a>

#### auth\_token

```python
@property
def auth_token() -> str
```

<a id="ratingsystems.core.data_source.DataSource.auth_token"></a>

#### auth\_token

```python
@auth_token.setter
def auth_token(value: str)
```

<a id="ratingsystems.core.data_source.DataSource.save"></a>

#### save

```python
def save(games: list[Game])
```

<a id="ratingsystems.core.data_source.DataSource.load"></a>

#### load

```python
def load(incomplete: bool = True) -> list[Game]
```

