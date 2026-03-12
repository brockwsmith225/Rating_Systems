# ratingsystems

This Python module defines 


---

# CLI

When you install the ratingsystems package, a CLI is included. You can use the following commands to run your rating systems.

### fetch
```
ratingsystems fetch --year <year> --data <datasource>
```
Used to fetch data for `<year>` using the `<datasource>` data source (Note: you must have the selected data source installed).


### rate
```
ratingsystems rate --year <year> --data <datasource> --rating <ratingsystem> --opt <opt>=<value> --opt <opt>=<value>
```
Used to rate teams for `<year>` with data from the `<datasource>` data source using the `<ratingsystem>` rating system (Note: you must have the selected data source and rating system installed). Any options will be passed to the rating system.


### predict
```
ratingsystems predict TEAM OPPONENT --year <year> --data <datasource> --rating <ratingsystem> --predictor <predictor> --opt <opt>=<value> --opt <opt>=<value>
```
Used to predict a matchup of `TEAM` and `OPPONENT` for `<year>` with data from the `<datasource>` data source and ratings from the `<ratingsystem>` rating system using the `<predictor>` predictor (Note: you must have the selected data source, rating system, and predictor installed). Any options will be passed to the rating system and predictor.


### config
```
ratingsystems config --year <year> --data <datasource> --rating <ratingsystem> --predictor <predictor> --opt <opt>=<value> --opt <opt>=<value>
```
Used to setup configurations that will persist. (Note: this will only persist options while in an interactive shell)

## Interactive Shell

You can run `ratingsystems` to start an interactive shell. In this shell you can run any of the above commands (omitting the `ratingsystems` part). State will persist across commands. This may for example be helpful when running multiple `predict` commands, especially if the rating system takes a long time to run.


---

# Plugins

The ratingsystems module provides a few base objects which can be used to create plugins.

### CLI 

Plugins will automatically get picked up by the CLI if you include the following in your `pyproject.toml`. (Note: any changes to the `pyproject.toml` will require you to reinstall the package for the change to be picked up)

```
[project.entry-points.ratingsystems]
cbb = "ratingsystems.data:CBBDataSource"
```


## Data Sources

Data Sources are created using the [`DataSource`](docs.md#ratingsystems.core.data_source.DataSource) class.


## Rating Systems

Rating Systems are created using the [`RatingSystem`](docs.md#ratingsystems.core.rating_system.RatingSystem) class.


## Predictors

Predictors are created using the [`Predictor`](docs.md#ratingsystems.core.predictor.Predictor) class.
