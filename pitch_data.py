from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os
import requests
from urllib.request import urlopen
import plotly.express as px

# baseball reference standard pitching webpage
br_url = 'https://www.baseball-reference.com/leagues/MLB/2020-standard-pitching.shtml'

team_labels = []
pitchers_used = []
average_pitchAge = []
runs_allowed_pgame = []
wins = []
losses = []
win_perc = []
team_era = []
games_started = []
games_finshed = []
complete_games = []
team_saves = []
hits_allowed = []
hr_allowed = []
walks_allowed = []
strikeouts = []
era_plus = []
team_fip = []
hits_pernine = []
hr_pernine = []
walks_pernine = []
strikeouts_pernine = []
SO_per_walk = []
runners_left = []
team_WHIP = []

# compiles lists or array of stats from Baseball Reference
def compileTeamPitch():

    # scraping object
    html = urlopen(br_url)
    bsObj = BeautifulSoup(html)


    # generating team names list
    team_labels_raw = bsObj.find_all('th', {'class': 'left', 'scope':'row', 'data-stat':'team_ID'})

    for item in team_labels_raw:
        item_text = item.get_text()
        team_labels.append(item_text)

    # generating pitcher used array
    pitchers_used_raw = bsObj.find_all('td', {'class': 'right', 'data-stat':'pitchers_used'})

    for item in pitchers_used_raw:
        item_text = item.get_text()
        pitchers_used.append(item_text)

    numPitch = pd.to_numeric(pitchers_used)

    # generating avergae pitching age array
    pitchAge_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'age_pitch'})

    for item in pitchAge_raw:
        item_text = item.get_text()
        average_pitchAge.append(item_text)

    pAge = pd.to_numeric(average_pitchAge)

    # generating runs allowed per game array
    runs_allowed_pgame_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'runs_allowed_per_game'})

    for item in runs_allowed_pgame_raw:
        item_text = item.get_text()
        runs_allowed_pgame.append(item_text)

    RAG = pd.to_numeric(runs_allowed_pgame)

    # generating wins array
    wins_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'W'})

    for item in wins_raw:
        item_text = item.get_text()
        wins.append(item_text)

    W = pd.to_numeric(wins)

    # generating losses array
    losses_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'L'})

    for item in losses_raw:
        item_text = item.get_text()
        losses.append(item_text)

    L = pd.to_numeric(losses)

    # generating win percentage array
    wins_perc_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'win_loss_perc'})

    for item in wins_perc_raw:
        item_text = item.get_text()
        win_perc.append(item_text)

    winPerc = pd.to_numeric(win_perc)

    # generating ERA array
    team_era_raw = bsObj.find_all('td', {'class':'right poptip', 'data-stat':'earned_run_avg'})

    for item in team_era_raw:
        item_text = item.get_text()
        team_era.append(item_text)

    team_era.append('')
    team_era.append('')

    ERA = pd.to_numeric(team_era)

    # generating games started array
    games_started_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'GS'})

    for item in games_started_raw:
        item_text = item.get_text()
        games_started.append(item_text)

    GS = pd.to_numeric(games_started)

    # generating games finished array
    games_finished_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'GF'})

    for item in games_finished_raw:
        item_text = item.get_text()
        games_finshed.append(item_text)

    GF = pd.to_numeric(games_finshed)

    # generating number of complete games array
    complete_games_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'CG'})

    for item in complete_games_raw:
        item_text = item.get_text()
        complete_games.append(item_text)

    CG = pd.to_numeric(complete_games)

    # generating number of team saves array
    team_saves_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'SV'})

    for item in team_saves_raw:
        item_text = item.get_text()
        team_saves.append(item_text)

    SV = pd.to_numeric(team_saves)

    # generating hits allowed array
    hits_allowed = []

    hits_allowed_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'H'})

    for item in hits_allowed_raw:
        item_text = item.get_text()
        hits_allowed.append(item_text)

    HA = pd.to_numeric(hits_allowed)

    # generating home runs allowed array
    hr_allowed_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'HR'})

    for item in hr_allowed_raw:
        item_text = item.get_text()
        hr_allowed.append(item_text)

    HRA = pd.to_numeric(hr_allowed)

    # generating walks allowed array
    walks_allowed_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'BB'})

    for item in walks_allowed_raw:
        item_text = item.get_text()
        walks_allowed.append(item_text)

    BB = pd.to_numeric(walks_allowed)


    # generating number of strikeouts array
    strikeouts_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'SO'})

    for item in strikeouts_raw:
        item_text = item.get_text()
        strikeouts.append(item_text)

    SO = pd.to_numeric(strikeouts)

    # generating ERA+ array
    era_plus_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'earned_run_avg_plus'})

    for item in era_plus_raw:
        item_text = item.get_text()
        era_plus.append(item_text)

    ERA_plus = pd.to_numeric(era_plus)

    # generating FIP array
    team_fip_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'fip'})

    for item in team_fip_raw:
        item_text = item.get_text()
        team_fip.append(item_text)

    FIP = pd.to_numeric(team_fip)

    # generating hits per nine innings array
    hits_pernine_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'hits_per_nine'})

    for item in hits_pernine_raw:
        item_text = item.get_text()
        hits_pernine.append(item_text)

    H9 = pd.to_numeric(hits_pernine)

    # generating home runs per nine array
    hr_pernine_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'home_runs_per_nine'})

    for item in hr_pernine_raw:
        item_text = item.get_text()
        hr_pernine.append(item_text)

    HR9 = pd.to_numeric(hr_pernine)

    # generating walks per nine innings array
    walks_pernine_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'bases_on_balls_per_nine'})

    for item in walks_pernine_raw:
        item_text = item.get_text()
        walks_pernine.append(item_text)

    BB9 = pd.to_numeric(walks_pernine)

    # generating strikeouts per nine array
    strikeouts_pernine_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'strikeouts_per_nine'})

    for item in strikeouts_pernine_raw:
        item_text = item.get_text()
        strikeouts_pernine.append(item_text)

    SO9 = pd.to_numeric(strikeouts_pernine)

    # generating strikeouts to walk ratio array
    SO_per_walk_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'strikeouts_per_base_on_balls'})

    for item in SO_per_walk_raw:
        item_text = item.get_text()
        SO_per_walk.append(item_text)

    SOBB = pd.to_numeric(SO_per_walk)

    # generating runners left on base array
    runners_left_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'LOB'})

    for item in runners_left_raw:
        item_text = item.get_text()
        runners_left.append(item_text)

    LOB = pd.to_numeric(runners_left)

    # generating WHIP array
    WHIP_raw = bsObj.find_all('td', {'class':'right', 'data-stat':'whip'})

    for item in WHIP_raw:
        item_text = item.get_text()
        team_WHIP.append(item_text)

    WHIP = pd.to_numeric(team_WHIP)

    # organize data from list/array form to dataframe
    def toDataframe():

        team_pitching = {'Team':team_labels, 'Pitchers Used':numPitch, 'Avg Age':pAge, 'RA/G':RAG,
        'Wins':W, 'Losses':L, 'Win %':winPerc, 'ERA':ERA, 'Games Started':GS, 'Games Finished':GF,
        'Complete Games':CG, 'Saves':SV, 'Hits Allowed':HA, 'HR Allowed':HRA, 'Walks':BB,
        'Strikeouts':SO, 'ERA+':ERA_plus, 'FIP':FIP, 'H/9':H9, 'HR/9':HR9, 'BB/9':BB9, 'SO/9':SO9,
        'SO/BB':SOBB, 'Runner Left':LOB, 'WHIP':WHIP}
        team_pitching_df = pd.DataFrame(team_pitching)

        return team_pitching_df

    frame = toDataframe()
    return frame
