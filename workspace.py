import urllib.request
import json
import pprint
from config import RIOTAPI
import ssl
#allow for url to be analyzed correctly 
ssl._create_default_https_context = ssl._create_unverified_context

#obtain the puuid from a user, using username and tagline
def get_puuid(username,tagline):
    #create custom url using username tagline and apikey
    url = 'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/' + username + '/' + tagline + '?api_key=' + RIOTAPI
    #decode json file and obtain data
    with urllib.request.urlopen(url) as f:
        repsonse_text = f.read().decode('utf-8')
        data = json.loads(repsonse_text)
    #return the puuid from the dictionary 'data'
    return data['puuid']
#obtain the matchid using puuid
def get_matchid(puuid):
    #create custom url using puuid and api key
    url = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/' + puuid + '/ids?start=0&count=20&api_key=' + RIOTAPI
    #decode json file
    with urllib.request.urlopen(url) as f:
        repsonse_text = f.read().decode('utf-8')
        data = json.loads(repsonse_text)
    #return data
    return data

#get the overall match stats for each player using match id and api key 
def get_match_stats(match_id):
    url = 'https://americas.api.riotgames.com/lol/match/v5/matches/' + match_id + '?api_key=' + RIOTAPI
    #decode json
    with urllib.request.urlopen(url) as f:
        repsonse_text = f.read().decode('utf-8')
        data = json.loads(repsonse_text)
    #return data
    return data

#get the number of kills for a given player using matchdata.
#Find given player by searching for matching summonername. Return the kills. This is a starter function.
def get_kills(matchdata):
    playerdict = {}
    for i in range(len(matchdata['info']['participants'])):
        playerdict[matchdata['info']['participants'][i]['summonerName']] = matchdata['info']['participants'][i]['kills']
    return(playerdict)
#return a list of the players in the match by using matchdata dictionary
def get_players(matchdata):
    playerlist = []
    for i in range(len(matchdata['info']['participants'])):
        playerlist.append([matchdata['info']['participants'][i]['summonerName']])
    return playerlist

#get the number of kills for a given player using matchdata.
#Find given player by searching for matching summonername. Return the number of baitPings
def get_player_baitPings(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['baitPings']

#get the number of kills for a given player using matchdata.
#Find given player by searching for matching summonername. Return the number of kills
def get_player_kills(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['kills']

#get the number of deaths for a given player using matchdata.
#Find given player by searching for matching summonername. Return the number of deaths
def get_player_deaths(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['deaths']

#get the number of assists for a given player using matchdata.
#Find given player by searching for matching summonername. Return the number of assists
def get_player_assists(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['assists']

#get the Vision Score for a given player using matchdata.
#Find given player by searching for matching summonername. Return the Vision Score
def get_player_visionScore(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['visionScore']

#get the positoin for a given player using matchdata.
#Find given player by searching for matching summonername. Return the Position of the Player
def get_player_teamPosition(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['teamPosition']

#get the total damage for a given player using matchdata.
#Find given player by searching for matching summonername. Return the total damage
def get_player_totaldamage(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['totalDamageDealt']

#get the champion name for a given player using matchdata.
#Find given player by searching for matching summonername. Return the Champion Name
def get_player_championName(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['championName']

#get the Objective Damage for a given player using matchdata.
#Find given player by searching for matching summonername. Return the total Objective Damage
def get_player_ObejctiveDamage(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['damageDealtToObjectives']

#get the Turret Damage for a given player using matchdata.
#Find given player by searching for matching summonername. Return the total Turret Damage
def get_player_TurretDamage(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['damageDealtToTurrets']

#get the Gold Earned for a given player using matchdata.
#Find given player by searching for matching summonername. Return the total Gold Earned
def get_player_goldEarned(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['goldEarned']

#get the number of pinkWards purchased for a given player using matchdata.
#Find given player by searching for matching summonername. Return the total number of Pink Wards
def get_player_pinkWards(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['sightWardsBoughtInGame']

#get the Total Damage Dealt to other players for a given player using matchdata.
#Find given player by searching for matching summonername. Return the total Damage to Champions
def get_player_TotalDamagetoChampions(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['totalDamageDealtToChampions']

#get the Creep Score for a given player using matchdata.
#Find given player by searching for matching summonername. Return the total Creep Score
def get_player_CreepScore(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['totalMinionsKilled']

#get the Time Spent Dead for a given player using matchdata.
#Find given player by searching for matching summonername. Return the total Time Spent Dead
def get_player_timeSpentDead(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['totalTimeSpentDead']

#get the number of Turret Takedowns for a given player using matchdata.
#Find given player by searching for matching summonername. Return the total Turret Takedowns
def get_player_turretTakedowns(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['turretTakedowns']

#return the match id using matchdata as an input
def get_match_id(matchdata):
    return matchdata['metadata']['matchId']

#testing
def main():
    
   # get_puuid('SchtankyLeg','PANTS')
    #get_matchid(get_puuid('SchtankyLeg','PANTS'))
    # x= (get_match_stats(get_matchid(get_puuid('QuickPlatinum','NA1'))[0]))
    # print(len(x['info']['participants']))
    # print (x['info']['participants'][0]['baitPings'])
    # for i in range(len(x['info']['participants'])):
    #     if x['info']['participants'][i]['summonerName']=="QuickPlatinum":
    #         index = int(i)
    #         print(index)
    # print(x['info']['participants'][index]['baitPings'])

    # print(get_player_championName('QuickPlatinum', 'NA1_4504131447'))
    #print(get_player_baitPings(get_match_stats(get_matchid(get_puuid('QuickPlatinum','NA1'))[0])))
    #print(get_puuid('QuickPlatinum','NA1'))
    #print(get_player_kills("QuickPlatinum", 'NA1_4504131447'))
    #print(get_player_stats(match,'QuickPlatinum'))
    #get_kills(get_match_stats(get_matchid(get_puuid('QuickPlatinum','NA1'))[0]))
    pass
#run program
if __name__== '__main__':
    print(main())