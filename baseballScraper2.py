#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 00:00:40 2018

@author: rishi
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

playerID = "harpebr03"

file = open("final2018ids", "r")
ids = file.read()
idList = ids.split('\n')
year = "2018"

battingLogDict = {}

for i in range(330, len(idList)):
    url = requests.get("https://www.baseball-reference.com/players/gl.fcgi?id=" + idList[i] + "&t=b&year=" + year).text
    soup = BeautifulSoup(url, 'lxml')
    table = soup.find('table',id='batting_gamelogs')
    
    sBuilder = ""
    for row in table.findAll('tr'):
        columns = row.findAll('td')
        for x in columns:
            sBuilder += x.text + '|'
        sBuilder += '\n'
        
    seasonGameNumber = []
    dateOfGame = []
    teamOfBatter = []
    homeOrAway = []
    opposingTeam = []
    plateAppearances = []
    atBats = []
    hits = []
    walks = []
    intentionalWalks = []
    battingAverage = []
    onBasePercentage = []
    sluggingPercentage = []
    pressureIndex = []
    
    # 1: Season game number for team
    # 2: Date of game
    # 3: Team of batter
    # 4: Home or away
    # 5: Batter's opponent
    # 8: Plate appearances
    # 9: At-bats
    # 11: Hits
    # 16: BB
    # 17: IBBs
    # 26: Current season batting average
    # 27: On-base percentage
    # 28: Slugging percentage
    # 31: Average leverage index (pressure)
    
    rowsArr = sBuilder.split('\n')
    for row in rowsArr:
        sub = row.split('|')
        if (len(sub) > 30):
            seasonGameNumber.append(sub[1])
            dateOfGame.append(sub[2])
            teamOfBatter.append(sub[3])
            homeOrAway.append(sub[4])
            opposingTeam.append(sub[5])
            plateAppearances.append(sub[8])
            atBats.append(sub[9])
            hits.append(sub[11])
            walks.append(sub[16])
            intentionalWalks.append(sub[17])
            battingAverage.append(sub[26])
            onBasePercentage.append(sub[27])
            sluggingPercentage.append(sub[28])
            pressureIndex.append(sub[31])
    
    batterGameLogData = pd.DataFrame({
        'GameNumber': seasonGameNumber,
        'Date': dateOfGame,
        'Team': teamOfBatter,
        'HomeOrAway': homeOrAway,
        'Opponent': opposingTeam,
        'PA': plateAppearances,
        'AB': atBats,
        'Hits': hits,
        'Walks': walks,
        'IBB': intentionalWalks,
        'BA': battingAverage,
        'OBP': onBasePercentage,
        'SLG': sluggingPercentage,
        'ALI': pressureIndex
    })
    
    battingLogDict[idList[i]] = batterGameLogData
    
    print("added player " + str(i) + " " + idList[i] + " to dict")
    



