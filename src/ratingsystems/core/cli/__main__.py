import cbbd
import cfbd
import math
import networkx as nx
import numpy as np
import pickle
from statistics import mean, median

import click
from click_shell import shell

from ratingsystems.common.model.bracket import Bracket
from ratingsystems.common.model.rating import Rating
from ratingsystems.common.predictor import AggregatePredictor, RatingDifferencePredictor

from ratingsystems.cer import CompleteEfficiencyRatingSystem
from ratingsystems.cer.predictor import CompleteEfficiencyRatingPredictor
from ratingsystems.rrs import RelativeRatingSystem
from ratingsystems.rrs.predictor import RelativeRatingSystemMarkovChainPredictor
from ratingsystems.rrs.model.stat import PageRank
from ratingsystems.ser import SimpleEfficiencyRatingSystem
from ratingsystems.ser.predictor import SimpleEfficiencyPredictor
from ratingsystems.zer import ZscoreEfficiencyRatingSystem

WIN_WEIGHT = 10
MAXIMUM_MOV = 99999
ALPHA = 0.5
MAXIMUM_ITERATIONS = 10000


def cfb(fetch_data = True):
    if fetch_data:
        configuration = cfbd.Configuration(
            access_token=''
        )
        games_api = cfbd.GamesApi(cfbd.ApiClient(configuration))

        games = []
        year = 2025
        week = 15
        for w in range(1, week + 1):
            games.extend(games_api.get_games(year, week=w, classification="fbs", season_type="regular"))
        # games.extend(games_api.get_games(year, classification="fbs", season_type="both"))

        games = [g for g in games if g.home_points is not None and g.away_points is not None and g.home_classification.value == "fbs" and g.away_classification.value == "fbs"]
        # games.extend(games_api.get_games(2024, classification="fcs"))
    #     with open("2024.games", "w") as f:
    #         pickle.dump(games, f)
    # else:
    #     with open("2024.games", "r") as f:
    #         games = pickle.load(f)

    print(mean([abs(g.home_points - g.away_points) for g in games]))
    print(median([abs(g.home_points - g.away_points) for g in games]))

    rrs_rating = rrs(games, win_weight=15)
    ser_rating = ser(games, k=1)
    # ser_rating = ser(games, seed=rrs_rating)

    # combined_rating = ((rrs_rating.rating + ser_rating.rating * abs(rrs_rating.rating)) * 1000) % "combined"
    combined_rating = (ser_rating.rating + rrs_rating.rating) / 2 % "combined"
    # combined_rating = (abs(ser_rating.rating) * rrs_rating.rating * 833) % "combined"
    rrs_rankings = {t.name: i + 1 for i, t in enumerate(Rating.rank(combined_rating.rrs))}
    rrs_wins_rankings = {t.name: i + 1 for i, t in enumerate(Rating.rank(combined_rating.rrs.win))}
    rrs_losses_rankings = {t.name: i + 1 for i, t in enumerate(Rating.rank(combined_rating.rrs.loss))}
    ser_rankings = {t.name: i + 1 for i, t in enumerate(Rating.rank(combined_rating.ser))}
    ser_offense_rankings = {t.name: i + 1 for i, t in enumerate(Rating.rank(combined_rating.ser.offense))}
    ser_defense_rankings = {t.name: i + 1 for i, t in enumerate(Rating.rank(combined_rating.ser.defense, reverse=True))}

    r = 1
    for team in Rating.rank(combined_rating.rating):
        wins = sum([1 for game in games if (game.home_team == team.name and game.completed and game.home_points > game.away_points) or (game.away_team == team.name and game.completed and game.away_points > game.home_points)])
        losses = sum([1 for game in games if (game.home_team == team.name and game.completed and game.away_points > game.home_points) or (game.away_team == team.name and game.completed and game.home_points > game.away_points)])
        # print(f"{r:5} | {team.name:25} | {f'({wins}-{losses})':>10} | {team.rating:>10} {f'({r})':>5} | {team.ser.rating:>10} {f'({ser_rankings[team.name]})':>5} | {team.rrs.rating:>10} {f'({rrs_rankings[team.name]})':>5}")
        print(f"{r},{team.name},{wins}-{losses},{team.rating.value},,,,{team.ser.rating.value},{ser_rankings[team.name]},{team.ser.offense.rating.value},{ser_offense_rankings[team.name]},{team.ser.defense.rating.value},{ser_defense_rankings[team.name]},,,{team.rrs.rating.value},{rrs_rankings[team.name]},{team.rrs.win.rating.value},{rrs_wins_rankings[team.name]},{team.rrs.loss.rating.value},{rrs_losses_rankings[team.name]}")
        r += 1

def stats():
    configuration = cfbd.Configuration(
        access_token=''
    )
    games_api = cfbd.GamesApi(cfbd.ApiClient(configuration))

    year = 2024

    teams = set()
    game_stats = []
    games = games_api.get_games(year, classification="fbs", season_type="both")
    # for game in games:
    #     # if game.home_classification == "fbs" and game.home_team not in teams:
    #     #     print(game.home_team)
    #     #     teams.add(game.home_team)
    #     #     game_stats.extend(games_api.get_team_game_stats(year, team=game.home_team, season_type="both"))
    #     # if game.away_classification == "fbs" and game.away_team not in teams:
    #     #     teams.add(game.away_team)
    #     #     game_stats.extend(games_api.get_team_game_stats(year, team=game.away_team, season_type="both"))
    #     game_stats.extend(games_api.get_team_game_stats(year, game_id=game.id, season_type="both"))
    #     print(game_stats)
    # print(len(teams))

    # for game in game_stats:
    #     print(f"{game.points},{game.points},{game.stats}")

    points = {}
    points_against = {}
    opponents = {}

    for game in games:
        if not game.completed:
            continue
        if game.home_classification != "fbs":
            continue
        if game.away_classification != "fbs":
            continue
        if game.home_team not in points:
            points[game.home_team] = []
            points_against[game.home_team] = []
            opponents[game.home_team] = []
        points[game.home_team].append(game.home_points)
        points_against[game.home_team].append(game.away_points)
        opponents[game.home_team].append(game.away_team)
        if game.away_team not in points:
            points[game.away_team] = []
            points_against[game.away_team] = []
            opponents[game.away_team] = []
        points[game.away_team].append(game.away_points)
        points_against[game.away_team].append(game.home_points)
        opponents[game.away_team].append(game.home_team)

    avg_points = {t: sum(p) / len(p) for t, p in points.items()}
    avg_points_against = {t: sum(p) / len(p) for t, p in points_against.items()}

    ser_rating = ser(games)
    rrs_rating = rrs(games)

    for team in points.keys():
        for i in range(len(points[team])):
            p = points[team][i]
            pa = points_against[team][i]
            opponent = opponents[team][i]
            avg_p = avg_points[team]
            avg_pa = avg_points_against[opponent]
            off_eff = p / avg_pa - 1
            def_eff = 1 - p / avg_p
            avg_off_eff = ser_rating.offense.get(team).value
            avg_def_eff = ser_rating.defense.get(opponent).value
            r = rrs_rating.get(team).value * 10000
            opp_r = rrs_rating.get(opponent).value * 10000
            print(f"{team},{opponent},{avg_p},{avg_pa},{avg_off_eff},{avg_def_eff},{avg_off_eff - avg_def_eff},{p},{off_eff},{def_eff},{p - avg_p},{off_eff - avg_off_eff},{p - avg_pa},{def_eff - avg_off_eff},{avg_p - avg_pa},{r},{opp_r},{r - opp_r},{p - pa}")

def predict(fetch_data: bool = True):
    if fetch_data:
        configuration = cfbd.Configuration()
        configuration.api_key['Authorization'] = ''
        configuration.api_key_prefix['Authorization'] = 'Bearer'
        games_api = cfbd.GamesApi(cfbd.ApiClient(configuration))

        games = []
        year = 2024
        # for week in range(1, 13):
        #     print(week)
        #     games.extend(games_api.get_games(year, week=week, classification="fbs", season_type="both"))
        games.extend(games_api.get_games(year, classification="fbs", season_type="both"))
        # games.extend(games_api.get_games(2024, classification="fcs"))
    #     with open("2024.games", "w") as f:
    #         pickle.dump(games, f)
    # else:
    #     with open("2024.games", "r") as f:
    #         games = pickle.load(f)
    rrs_rating = rrs(games)
    ser_rating = ser(games)
    combined_rating = (ser_rating.rating * 22 + rrs_rating.rating * 991) / 2 % "combined"

    matchups = [
        # ("Ohio State", "Tennessee"),
        #     ("Oregon", "Ohio State"), ("Oregon", "Tennessee"),
        # ("Texas", "Clemson"),
        #     ("Arizona State", "Texas"), ("Arizona State", "Clemson"),
        # ("Penn State", "SMU"),
        #     ("Boise State", "Penn State"), ("Boise State", "SMU"),
        # ("Notre Dame", "Indiana"),
        #     ("Georgia", "Notre Dame"), ("Georgia", "Indiana"),
        # ("Oregon", "Texas"), ("Notre Dame", "Penn State"),
        #     ("Oregon", "Notre Dame"), ("Oregon", "Penn State"), ("Texas", "Notre Dame"), ("Texas", "Penn State"),
        # ("Notre Dame", "Georgia"),
        # ("Ohio State", "Texas"),
        # ("Penn State", "Notre Dame"),
        # ("Penn State", "Georgia"),
        ("Ohio State", "Notre Dame")
    ]

    for team, opponent in matchups:
        print("===============================================")
        rrs_prediction = rrs_predict(rrs_rating, team, opponent)
        rrs_markov_prediction = rrs_predict_markov_chain(rrs_rating, team, opponent)
        ser_prediction = ser_predict(ser_rating, team, opponent)
        print(f"rrs: {rrs_prediction}")
        print(f"rrs markov: {rrs_markov_prediction}")
        print(f"ser: {ser_prediction}")
        # print(f"ser total: {ser_predict_total(ser_rating, team, opponent)}")
        print(f"average: {sum([p.odds for p in [rrs_markov_prediction, ser_prediction]]) / 2} [{sum([p.line for p in [rrs_markov_prediction, ser_prediction]]) / 2}]")
        print(f"aggregate: {RatingDifferencePredictor().predict(combined_rating, team, opponent)}")


def rrs(games: list, win_weight: int = 30):
    rrs = RelativeRatingSystem(
        win_weight=win_weight,
        alpha=0.5,
        max_mov=None,
        # do_baseline_adjustment=False,
        add_sink=True,
    )
    return rrs.rate(games)


def rrs_predict(rating: Rating, team: str, opponent: str):
    rrs = RelativeRatingSystemPredictor()
    return rrs.predict(rating, team, opponent)


def rrs_predict_markov_chain(rating: Rating, team: str, opponent: str):
    rrs = RelativeRatingSystemMarkovChainPredictor()
    return rrs.predict(rating, team, opponent)


def ser(games: list, seed: Rating = None, k: float = 8.0):
    ser = SimpleEfficiencyRatingSystem(
        k=k
    )
    return ser.rate(games, seed=seed)

def ser_predict(rating: Rating, team: str, opponent: str):
    ser = RatingDifferencePredictor()
    return ser.predict(rating, team, opponent)

def ser_predict_total(rating: Rating, team: str, opponent: str):
    ser = SimpleEfficiencyPredictor()
    return ser.predict(rating, team, opponent)


def zer(games: list, seed: Rating = None):
    zer = ZscoreEfficiencyRatingSystem(
        
    )
    return zer.rate(games, seed=seed)


def cer(games: list, seed: Rating = None):
    cer = CompleteEfficiencyRatingSystem(
        include_points=True,
    )
    return cer.rate(games, seed=seed)


def cbb(fetch_data = True):
    if fetch_data:
        configuration = cbbd.Configuration(
            access_token=''
        )
        games_api = cbbd.GamesApi(cbbd.ApiClient(configuration))

        games = []
        team_games = []
        year = 2026
        # week = 16
        # for w in range(1, week + 1):
        #     print(w)
        #     games.extend(games_api.get_games(year, week=w, classification="fbs", season_type="regular"))
        games.extend(games_api.get_games(season=year, season_type="regular", status=cbbd.GameStatus("final"), start_date_range=f"{year-1}-11-01T00:00:00", end_date_range=f"{year-1}-11-30T23:59:59"))
        games.extend(games_api.get_games(season=year, season_type="regular", status=cbbd.GameStatus("final"), start_date_range=f"{year-1}-12-01T00:00:00", end_date_range=f"{year-1}-12-31T23:59:59"))
        games.extend(games_api.get_games(season=year, season_type="regular", status=cbbd.GameStatus("final"), start_date_range=f"{year}-01-01T00:00:00", end_date_range=f"{year}-01-31T23:59:59"))
        games.extend(games_api.get_games(season=year, season_type="regular", status=cbbd.GameStatus("final"), start_date_range=f"{year}-02-01T00:00:00", end_date_range=f"{year}-02-28T23:59:59"))
        games.extend(games_api.get_games(season=year, season_type="regular", status=cbbd.GameStatus("final"), start_date_range=f"{year}-03-01T00:00:00", end_date_range=f"{year}-03-31T23:59:59"))
        games.extend(games_api.get_games(season=year, season_type="postseason", status=cbbd.GameStatus("final"), start_date_range=f"{year}-03-01T00:00:00", end_date_range=f"{year}-03-31T23:59:59"))

        team_games.extend(games_api.get_game_teams(season=year, season_type="regular", start_date_range=f"{year-1}-11-01T00:00:00", end_date_range=f"{year-1}-11-30T23:59:59"))
        team_games.extend(games_api.get_game_teams(season=year, season_type="regular", start_date_range=f"{year-1}-12-01T00:00:00", end_date_range=f"{year-1}-12-31T23:59:59"))
        team_games.extend(games_api.get_game_teams(season=year, season_type="regular", start_date_range=f"{year}-01-01T00:00:00", end_date_range=f"{year}-01-31T23:59:59"))
        team_games.extend(games_api.get_game_teams(season=year, season_type="regular", start_date_range=f"{year}-02-01T00:00:00", end_date_range=f"{year}-02-28T23:59:59"))
        team_games.extend(games_api.get_game_teams(season=year, season_type="regular", start_date_range=f"{year}-03-01T00:00:00", end_date_range=f"{year}-03-31T23:59:59"))
        team_games.extend(games_api.get_game_teams(season=year, season_type="postseason", start_date_range=f"{year}-03-01T00:00:00", end_date_range=f"{year}-03-31T23:59:59"))
        # games.extend(games_api.get_games(2024, classification="fcs"))
    #     with open("2024.games", "w") as f:
    #         pickle.dump(games, f)
    # else:
    #     with open("2024.games", "r") as f:
    #         games = pickle.load(f)

    # print(mean([abs(g.home_points - g.away_points) for g in games]))
    # print(median([abs(g.home_points - g.away_points) for g in games]))

    games = [game for game in games if game.status.value == "final" and game.home_conference is not None and game.away_conference is not None]
    team_games = [game for game in team_games if game.game_minutes is not None and game.conference is not None and game.opponent_conference is not None]
    rrs_rating = rrs(games, win_weight=12)  # win_weight=15 (??)
    ser_rating = ser(games)
    zer_rating = zer(games)
    cer_rating = cer(team_games)
    # ser_rating = ser(games, seed=rrs_rating)

    ser_weight = 0 / ser_rating.stdev
    zer_weight = 0 / zer_rating.stdev
    cer_weight = 1 / cer_rating.stdev
    resume_rating = rrs_rating % "resume"
    offensive_efficiency_rating = ((ser_rating.offense % "ser" * ser_weight + zer_rating.offense % "zer" * zer_weight + cer_rating.offense % "cer" * cer_weight) / (ser_weight + zer_weight + cer_weight)) % "offense"
    defensive_efficiency_rating = ((ser_rating.defense % "ser" * ser_weight + zer_rating.defense % "zer" * zer_weight + cer_rating.defense % "cer" * cer_weight) / (ser_weight + zer_weight + cer_weight)) % "defense"
    efficiency_rating = (offensive_efficiency_rating - defensive_efficiency_rating) % "efficiency" << cer_rating.tempo
    efficiency_rating = cer_rating % "efficiency"

    resume_weight = 1
    efficiency_weight = 1
    combined_rating = (resume_rating * resume_weight + efficiency_rating * efficiency_weight) / (resume_weight + efficiency_weight)

    resume_rankings = {t.name: i + 1 for i, t in enumerate(Rating.rank(combined_rating.resume))}
    resume_wins_rankings = {t.name: i + 1 for i, t in enumerate(Rating.rank(combined_rating.resume.win))}
    resume_losses_rankings = {t.name: i + 1 for i, t in enumerate(Rating.rank(combined_rating.resume.loss))}
    resume_sos_rankings = {t.name: i + 1 for i, t in enumerate(Rating.rank(combined_rating.resume.sos))}
    efficiency_rankings = {t.name: i + 1 for i, t in enumerate(Rating.rank(combined_rating.efficiency))}
    efficiency_offense_rankings = {t.name: i + 1 for i, t in enumerate(Rating.rank(combined_rating.efficiency.offense))}
    efficiency_defense_rankings = {t.name: i + 1 for i, t in enumerate(Rating.rank(combined_rating.efficiency.defense, reverse=True))}
    efficiency_tempo_rankings = {t.name: i + 1 for i, t in enumerate(Rating.rank(combined_rating.efficiency.tempo))}

    r = 1
    for team in Rating.rank(combined_rating):
        wins = sum([1 for game in games if (game.home_team == team.name and game.status.value == "final" and game.home_points > game.away_points) or (game.away_team == team.name and game.status.value == "final" and game.away_points > game.home_points)])
        losses = sum([1 for game in games if (game.home_team == team.name and game.status.value == "final" and game.away_points > game.home_points) or (game.away_team == team.name and game.status.value == "final" and game.home_points > game.away_points)])
        conference = [game.home_conference if game.home_team == team.name else game.away_conference for game in games if game.home_team == team.name or game.away_team == team.name][0]
        # print(f"{r:5} | {team.name:25} | {f'({wins}-{losses})':>10} | {team.rating:>10} {f'({r})':>5} | {team.efficiency.rating:>10} {f'({efficiency_rankings[team.name]})':>5} | {team.resume.rating:>10} {f'({resume_rankings[team.name]})':>5}")
        print(f"{r},{team.name},{wins}-{losses},{conference},{team.rating.value},{r},{team.efficiency.rating.value},{efficiency_rankings[team.name]},{team.efficiency.offense.rating.value},{efficiency_offense_rankings[team.name]},{team.efficiency.defense.rating.value},{efficiency_defense_rankings[team.name]},{team.efficiency.tempo.rating.value},{efficiency_tempo_rankings[team.name]},{team.resume.rating.value},{resume_rankings[team.name]},{team.resume.win.rating.value},{resume_wins_rankings[team.name]},{team.resume.loss.rating.value},{resume_losses_rankings[team.name]},{team.resume.sos.rating.value},{resume_sos_rankings[team.name]}")
        r += 1


def cbb_stats(fetch_data = True):
    if fetch_data:
        configuration = cbbd.Configuration(
            access_token=''
        )
        games_api = cbbd.GamesApi(cbbd.ApiClient(configuration))

        games = []
        year = 2025
        week = 16

        games.extend(games_api.get_games(season=year, season_type="regular", status=cbbd.GameStatus("final"), start_date_range=f"{year-1}-11-01T00:00:00", end_date_range=f"{year-1}-11-30T23:59:59"))
        games.extend(games_api.get_games(season=year, season_type="regular", status=cbbd.GameStatus("final"), start_date_range=f"{year-1}-12-01T00:00:00", end_date_range=f"{year-1}-12-31T23:59:59"))
        games.extend(games_api.get_games(season=year, season_type="regular", status=cbbd.GameStatus("final"), start_date_range=f"{year}-01-01T00:00:00", end_date_range=f"{year}-01-31T23:59:59"))
        games.extend(games_api.get_games(season=year, season_type="regular", status=cbbd.GameStatus("final"), start_date_range=f"{year}-02-01T00:00:00", end_date_range=f"{year}-02-28T23:59:59"))
        games.extend(games_api.get_games(season=year, season_type="regular", status=cbbd.GameStatus("final"), start_date_range=f"{year}-03-01T00:00:00", end_date_range=f"{year}-03-31T23:59:59"))

    games = [game for game in games if game.status.value == "final" and game.home_conference is not None and game.away_conference is not None]

    points = {}
    points_against = {}
    opponents = {}

    for game in games:
        if game.status.value != "final":
            continue
        if game.home_conference is None:
            continue
        if game.away_conference is None:
            continue
        if game.home_team not in points:
            points[game.home_team] = []
            points_against[game.home_team] = []
            opponents[game.home_team] = []
        points[game.home_team].append(game.home_points)
        points_against[game.home_team].append(game.away_points)
        opponents[game.home_team].append(game.away_team)
        if game.away_team not in points:
            points[game.away_team] = []
            points_against[game.away_team] = []
            opponents[game.away_team] = []
        points[game.away_team].append(game.away_points)
        points_against[game.away_team].append(game.home_points)
        opponents[game.away_team].append(game.home_team)

    avg_points = {t: sum(p) / len(p) for t, p in points.items()}
    avg_points_against = {t: sum(p) / len(p) for t, p in points_against.items()}

    ser_rating = ser(games)
    rrs_rating = rrs(games)

    for team in points.keys():
        for i in range(len(points[team])):
            p = points[team][i]
            pa = points_against[team][i]
            opponent = opponents[team][i]
            avg_p = avg_points[team]
            avg_pa = avg_points_against[opponent]
            off_eff = p / avg_pa - 1
            def_eff = 1 - p / avg_p
            avg_off_eff = ser_rating.offense.get(team).value
            avg_def_eff = ser_rating.defense.get(opponent).value
            r = rrs_rating.get(team).value * 10000
            opp_r = rrs_rating.get(opponent).value * 10000
            print(f"{team},{opponent},{avg_p},{avg_pa},{avg_off_eff},{avg_def_eff},{avg_off_eff - avg_def_eff},{p},{off_eff},{def_eff},{p - avg_p},{off_eff - avg_off_eff},{p - avg_pa},{def_eff - avg_off_eff},{avg_p - avg_pa},{r},{opp_r},{r - opp_r},{p - pa}")


def cbb_bracket(fetch_data = True):
    if fetch_data:
        configuration = cbbd.Configuration(
            access_token=''
        )
        games_api = cbbd.GamesApi(cbbd.ApiClient(configuration))

        games = []
        team_games = []
        year = 2025

        games.extend(games_api.get_games(season=year, season_type="regular", status=cbbd.GameStatus("final"), start_date_range=f"{year-1}-11-01T00:00:00", end_date_range=f"{year-1}-11-30T23:59:59"))
        games.extend(games_api.get_games(season=year, season_type="regular", status=cbbd.GameStatus("final"), start_date_range=f"{year-1}-12-01T00:00:00", end_date_range=f"{year-1}-12-31T23:59:59"))
        games.extend(games_api.get_games(season=year, season_type="regular", status=cbbd.GameStatus("final"), start_date_range=f"{year}-01-01T00:00:00", end_date_range=f"{year}-01-31T23:59:59"))
        games.extend(games_api.get_games(season=year, season_type="regular", status=cbbd.GameStatus("final"), start_date_range=f"{year}-02-01T00:00:00", end_date_range=f"{year}-02-28T23:59:59"))
        games.extend(games_api.get_games(season=year, season_type="regular", status=cbbd.GameStatus("final"), start_date_range=f"{year}-03-01T00:00:00", end_date_range=f"{year}-03-31T23:59:59"))
        games.extend(games_api.get_games(season=year, season_type="postseason", status=cbbd.GameStatus("final"), start_date_range=f"{year}-03-01T00:00:00", end_date_range=f"{year}-03-31T23:59:59"))

        team_games.extend(games_api.get_game_teams(season=year, season_type="regular", start_date_range=f"{year-1}-11-01T00:00:00", end_date_range=f"{year-1}-11-30T23:59:59"))
        team_games.extend(games_api.get_game_teams(season=year, season_type="regular", start_date_range=f"{year-1}-12-01T00:00:00", end_date_range=f"{year-1}-12-31T23:59:59"))
        team_games.extend(games_api.get_game_teams(season=year, season_type="regular", start_date_range=f"{year}-01-01T00:00:00", end_date_range=f"{year}-01-31T23:59:59"))
        team_games.extend(games_api.get_game_teams(season=year, season_type="regular", start_date_range=f"{year}-02-01T00:00:00", end_date_range=f"{year}-02-28T23:59:59"))
        team_games.extend(games_api.get_game_teams(season=year, season_type="regular", start_date_range=f"{year}-03-01T00:00:00", end_date_range=f"{year}-03-31T23:59:59"))
        team_games.extend(games_api.get_game_teams(season=year, season_type="postseason", start_date_range=f"{year}-03-01T00:00:00", end_date_range=f"{year}-03-31T23:59:59"))

    games = [game for game in games if game.status.value == "final" and game.home_conference is not None and game.away_conference is not None]
    team_games = [game for game in team_games if game.game_minutes is not None and game.conference is not None and game.opponent_conference is not None]

    rrs_rating = rrs(games)
    ser_rating = ser(games)
    zer_rating = zer(games)
    cer_rating = cer(team_games)

    ser_weight = 0 / ser_rating.stdev
    zer_weight = 0 / zer_rating.stdev
    cer_weight = 1 / cer_rating.stdev
    resume_rating = rrs_rating % "resume"
    offensive_efficiency_rating = ((ser_rating.offense % "ser" * ser_weight + zer_rating.offense % "zer" * zer_weight + cer_rating.offense % "cer" * cer_weight) / (ser_weight + zer_weight + cer_weight)) % "offense"
    defensive_efficiency_rating = ((ser_rating.defense % "ser" * ser_weight + zer_rating.defense % "zer" * zer_weight + cer_rating.defense % "cer" * cer_weight) / (ser_weight + zer_weight + cer_weight)) % "defense"
    efficiency_rating = (offensive_efficiency_rating - defensive_efficiency_rating) % "efficiency" << cer_rating.tempo
    efficiency_rating = cer_rating % "efficiency"

    efficiency_weight = 1
    resume_weight = 1
    combined_rating = (efficiency_rating * efficiency_weight + resume_rating * resume_weight) / (efficiency_weight + resume_weight)
    
    current_brackets = []
    current_bracket_name = None
    results = {}
    with open("../resources/data/cbb/2025.bracket", "r") as f:
        for line in f.readlines():
            if line.startswith("--"):
                current_bracket_name = line[2:].strip()
                continue

            if "!" in line:
                seed = int(line.split("!")[0].strip())
                team = line.split("!")[1].strip()
            else:
                team = line

            if "/" in team:
                team1 = team.split("/")[0]
                team2 = team.split("/")[1]
                if "~" in team1:
                    result = int(team1.split("~")[1])
                    team1 = team1.split("~")[0]
                    results[team1] = result
                if "~" in team2:
                    result = int(team2.split("~")[1])
                    team2 = team2.split("~")[0]
                    results[team2] = result
                bracket = Bracket(team1, team2, seed, seed, current_bracket_name)
            else:
                if "~" in team:
                    result = int(team.split("~")[1])
                    team = team.split("~")[0]
                    results[team] = result
                bracket = Bracket(team, None, seed, None, current_bracket_name)

            while len(current_brackets) > 0 and bracket.depth == current_brackets[-1].depth:
                bracket = Bracket(current_brackets.pop(), bracket)

            current_brackets.append(bracket)
    
    print(bracket)
    print(results)

    bracket.evaluate(RatingDifferencePredictor(combined_rating), results)

    bracket.evaluate(AggregatePredictor(
        CompleteEfficiencyRatingPredictor(efficiency_rating),
        RelativeRatingSystemMarkovChainPredictor(resume_rating),
        weights=[efficiency_weight, resume_weight],
    ), results)

    # bracket.evaluate(RatingDifferencePredictor(efficiency_rating), results)
    # first_odds = bracket.full_odds.copy()
    # bracket.evaluate(RatingDifferencePredictor(resume_rating), results)
    
    for team, value in bracket.full_odds.items():
        region, seed, odds = value
        print(f"{seed},{team},{combined_rating.get_value(team)},{region},{','.join([str(o) for o in odds])}")
        # print(f"{seed},{team},{combined_rating.get_value(team)},{region},{','.join([str(o * seed) for o in odds])}")
        # print(f"{seed},{team},{combined_rating.get_value(team)},{region},{','.join([str(o * math.sqrt(seed)) for o in odds])}")
        # print(f"{seed},{team},{combined_rating.get_value(team)},{region},{','.join([str(o - first_odds.get(team)[2][i]) for i, o in enumerate(odds)])}")


def cbb_test(fetch_data = True):
    if fetch_data:
        configuration = cbbd.Configuration(
            access_token=''
        )
        games_api = cbbd.GamesApi(cbbd.ApiClient(configuration))

        games = []
        year = 2025
        week = 16
        games.extend(games_api.get_game_teams(season=year, season_type="regular", start_date_range=f"{year-1}-11-01T00:00:00", end_date_range=f"{year-1}-11-30T23:59:59"))
        games.extend(games_api.get_game_teams(season=year, season_type="regular", start_date_range=f"{year-1}-12-01T00:00:00", end_date_range=f"{year-1}-12-31T23:59:59"))
        games.extend(games_api.get_game_teams(season=year, season_type="regular", start_date_range=f"{year}-01-01T00:00:00", end_date_range=f"{year}-01-31T23:59:59"))
        games.extend(games_api.get_game_teams(season=year, season_type="regular", start_date_range=f"{year}-02-01T00:00:00", end_date_range=f"{year}-02-28T23:59:59"))
        games.extend(games_api.get_game_teams(season=year, season_type="regular", start_date_range=f"{year}-03-01T00:00:00", end_date_range=f"{year}-03-31T23:59:59"))

    games = [game for game in games if game.game_minutes is not None and game.conference is not None and game.opponent_conference is not None]
    cer_rating = cer(games)

    # print(CompleteEfficiencyRatingPredictor(cer_rating).predict("Kansas", "Arkansas"))

    r = 1
    for team in Rating.rank(cer_rating):
        # print(f"{r}   {team.name}   {team.offense.rating.value}   {team.offense.shooting.rating.value}   {team.offense.rebounds.rating.value}   {team.offense.turnovers.rating.value}   {team.offense.free_throws.rating.value}")
        # print(f"{r}   {team.name}   {team.rating.value}   {team.offense.rating.value}   {team.defense.rating.value}   {team.defense.rebounds.rating.value}    {team.defense.shooting.rating.value}   {team.defense.shooting.two_pct.rating.value}   {team.defense.shooting.two_sel.rating.value}   {team.defense.shooting.three_pct.rating.value}   {team.defense.shooting.three_sel.rating.value}")
        print(f"{r}   {team.name}   {team.rating.value}   {team.offense.rating.value}   {team.defense.rating.value}")
        r += 1


if __name__ == "__main__":
    cfb()
    # stats()
    # predict()
    # cbb()
    # cbb_stats()
    # cbb_bracket()
    # cbb_test()