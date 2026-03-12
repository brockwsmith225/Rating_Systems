import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from typing import Optional, Union

from ratingsystems.core.model import Rating, Stat


def linear_regression(X: Union[list[float], list[list[float]]], y: list[float], weights: Optional[list[float]] = None, degree: int = 1, log: bool = False):
    if not isinstance(X[0], list):
        X = np.array(X).reshape(-1, 1)
    else:
        X = np.array(X)

    if log:
        X = np.log(X)

    if degree > 1:
        poly = PolynomialFeatures(degree=degree, include_bias=False)
        X = poly.fit_transform(X)

    y = np.array(y)

    model = LinearRegression()
    model.fit(X, y, weights)

    if degree > 1:
        return lambda *x: float(model.predict(np.array(poly.fit_transform([x])))[0])
    else:
        return lambda *x: float(model.predict(np.array([x]))[0])


def logistic_regression(X: Union[list[float], list[list[float]]], y: list[float], weights: Optional[list[float]] = None, degree: int = 1):
    if not isinstance(X[0], list):
        X = np.array(X).reshape(-1, 1)
    else:
        X = np.array(X)

    if degree > 1:
        poly = PolynomialFeatures(degree=degree, include_bias=False)
        X = poly.fit_transform(X)

    y = np.array(y)

    model = LogisticRegression()
    model.fit(X, y, weights)

    if degree > 1:
        return lambda *x: [float(p) for p in model.predict_proba(np.array(poly.fit_transform([x])))[0]]
    else:
        return lambda *x: [float(p) for p in model.predict_proba(np.array([x]))[0]]


def linear_regression_to_points(rating: Rating, games: list) -> Rating:
    X = []
    y = []
    if hasattr(games[0], "home_team"):
        average_points = sum([game.home_points + game.away_points for game in games]) / len(games) / 2
        for game in games:
            X.append([rating.get_value(game.home_team) - rating.get_value(game.away_team)])
            y.append(game.home_points - game.away_points)
            X.append([rating.get_value(game.away_team) - rating.get_value(game.home_team)])
            y.append(game.away_points - game.home_points)
    else:
        for game in games:
            X.append([rating.get_value(game.team) - rating.get_value(game.opponent)])
            y.append(game.team_stats.points.total - game.opponent_stats.points.total)
    model = LinearRegression()
    model.fit(np.array(X), np.array(y))
    return (rating * model.coef_[0] + model.intercept_) | Stat
