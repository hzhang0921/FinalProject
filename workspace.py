import urllib.request
import json
import pprint
from config import RIOTAPI



def get_puuid(username,tagline):
    url = 'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/' + username + '/' + tagline + '?api_key=' + RIOTAPI
    with urllib.request.urlopen(url) as f:
        repsonse_text = f.read().decode('utf-8')
        data = json.loads(repsonse_text)
    #pprint.pprint(data)
    #print (data['puuid'])
    return data['puuid']

def get_matchid(puuid):
    url = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/' + puuid + '/ids?start=0&count=20&api_key=' + RIOTAPI
    with urllib.request.urlopen(url) as f:
        repsonse_text = f.read().decode('utf-8')
        data = json.loads(repsonse_text)
    #pprint.pprint(data)
    return data

def get_match_stats(match_id):
    url = 'https://americas.api.riotgames.com/lol/match/v5/matches/' + match_id + '?api_key=' + RIOTAPI
    with urllib.request.urlopen(url) as f:
        repsonse_text = f.read().decode('utf-8')
        data = json.loads(repsonse_text)
    #pprint.pprint(data)
    return data

def get_kills(matchdata):
    playerdict = {}
    for i in range(len(matchdata['info']['participants'])):
        playerdict[matchdata['info']['participants'][i]['summonerName']] = matchdata['info']['participants'][i]['kills']
    return(playerdict)

def get_players(matchdata):
    playerlist = []
    for i in range(len(matchdata['info']['participants'])):
        playerlist.append([matchdata['info']['participants'][i]['summonerName']])
    return playerlist

def get_player_baitPings(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['baitPings']

def get_player_kills(matchdata, summonername):
    #print(range(len(matchdata['info']['participants'])))
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
            print(index)
    return matchdata['info']['participants'][index]['kills']

def get_player_deaths(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['deaths']

def get_player_assists(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['assists']

def get_player_visionScore(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['visionScore']

def get_player_teamPosition(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['teamPosition']

def get_player_totaldamage(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['totalDamageDealt']

def get_player_championName(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['championName']

def get_player_ObejctiveDamage(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['damageDealtToObjectives']

def get_player_TurretDamage(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['damageDealtToTurrets']

def get_player_goldEarned(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['goldEarned']

def get_player_pinkWards(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['sightWardsBoughtInGame']

def get_player_TotalDamagetoChampions(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['totalDamageDealtToChampions']

def get_player_CreepScore(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['totalMinionsKilled']

def get_player_timeSpentDead(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['totalTimeSpentDead']

def get_player_turretTakedowns(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            index = int(i)
    return matchdata['info']['participants'][index]['turretTakedowns']


def full_stats(summonername,tagline):
    puuid = get_puuid(summonername,tagline)
    match1 = get_matchid(puuid)[0]
    matchstats = get_match_stats(match1)
    kills = get_kills(matchstats)
    return kills


def main():
    
   # get_puuid('SchtankyLeg','PANTS')
    #get_matchid(get_puuid('SchtankyLeg','PANTS'))
    x= (get_match_stats(get_matchid(get_puuid('QuickPlatinum','NA1'))[0]))
    print(len(x['info']['participants']))
    print (x['info']['participants'][0]['baitPings'])
    for i in range(len(x['info']['participants'])):
        if x['info']['participants'][i]['summonerName']=="QuickPlatinum":
            index = int(i)
            print(index)
    print(x['info']['participants'][index]['baitPings'])

    print(get_player_championName('QuickPlatinum', 'NA1_4504131447'))
    #print(get_player_baitPings(get_match_stats(get_matchid(get_puuid('QuickPlatinum','NA1'))[0])))
    #print(get_puuid('QuickPlatinum','NA1'))
   # print(get_player_kills("QuickPlatinum", 'NA1_4504131447'))
    #print(get_player_stats(match,'QuickPlatinum'))
    #get_kills(get_match_stats(get_matchid(get_puuid('QuickPlatinum','NA1'))[0]))
    pass

if __name__== '__main__':
    print(main())