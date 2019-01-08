#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 22:26:22 2018

@author: rishi
"""

import pandas as pd
import numpy as np
from pybaseball import batting_stats_range
from pybaseball import playerid_lookup

class AllPlayers:

    def getAllPlayers(year):
        data = batting_stats_range(year + '-04-01', year + '-09-30')
        df = pd.DataFrame(data)
        allPlayers = df['Name'].tolist()
        return allPlayers

    def getPlayerIDs(players):
        listOfIDs = []
        for i in range (0, len(players)):
            splitPlayer = players[i].split(' ')
            first = splitPlayer[0]
            last = splitPlayer[1]                
            ident = playerid_lookup(last,first)
            identList = ident['key_bbref'].tolist()
            counter = len(identList) - 1
            
            if len(identList) > 0:    
                while str(identList[counter]) == 'nan' and counter > -1:
                    counter -= 1
                finalPlayerID = identList[counter]
                listOfIDs.append(finalPlayerID)
            else:
                listOfIDs.append("PLAYER NOT FOUND")
            
            print('added player ' + str(i))
            print(listOfIDs)
    
#    file = open("2018playerids.txt", "r")
#    ids = file.read()
#    idList = ids.split('\n')
#    playerNames = getAllPlayers('2018')
#    
#    idList[99] = 'boydma01'
#    idList[155] = 'chargtj01'
#    idList[170] = 'coleaj01'
#    idList[174] = 'conlopj01'
#    idList[187] = 'crawfjp01'
#    idList[188] = 'croncj01'
#    idList[203] = 'davisjd01'
#    idList[208] = 'rosajo01'
#    idList[209] = 'delosen01'
#    idList[213] = 'delmoni01'
#    idList[214] = 'dendema01'
#    idList[245] = 'ellisaj01'
#    idList[381] = 'happja01'
#    idList[454] = 'kangju01'
#    idList[485] = 'lasteto01'
#    idList[547] = 'martijd02'
#    idList[563] = 'mcfartj01'
#    idList[696] = 'polloaj01'
#    idList[716] = 'realmjt01'
#    idList[718] = 'reedaj01'
#    idList[833] = 'sneltdj01'
#    idList[885] = 'taylomi02'
#    idList[956] = 'wheelza01'
#
#    
#    finalFile = open("final2018ids", "w")
#    for x in idList:
#        finalFile.write(x + '\n')
#    finalFile.close()
#            
        
        
        
        
        
        
        
        
        
        