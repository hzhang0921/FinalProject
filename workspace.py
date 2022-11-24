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
    

def get_bait_pings(matchdata):
    playerdict = {}
    for i in range(len(matchdata['info']['participants'])):
        playerdict[matchdata['info']['participants'][i]['summonerName']] = matchdata['info']['participants'][i]['baitPings']
    return(playerdict)

def get_players(matchdata):
    playerlist = []
    for i in range(len(matchdata['info']['participants'])):
        playerlist.append([matchdata['info']['participants'][i]['summonerName']])
    return playerlist

def get_player_stats(matchdata, summonername):
    for i in range(len(matchdata['info']['participants'])):
        if matchdata['info']['participants'][i]['summonerName']==summonername:
            print(i)
            index = int(i)
    print("index")
    print(index)
    return matchdata['info']['participants'][index]['baitPings']

def full_stats(summonername,tagline):
    puuid = get_puuid(summonername,tagline)
    match1 = get_matchid(puuid)[0]
    matchstats = get_match_stats(match1)
    kills = get_kills(matchstats)
    return kills


def main():
    
   # get_puuid('SchtankyLeg','PANTS')
    #get_matchid(get_puuid('SchtankyLeg','PANTS'))
    match = get_match_stats(get_matchid(get_puuid('QuickPlatinum','NA1'))[0])
    #print(get_puuid('QuickPlatinum','NA1'))
    print(get_player_stats(match,'QuickPlatinum'))
    #get_kills(get_match_stats(get_matchid(get_puuid('QuickPlatinum','NA1'))[0]))
    pass

if __name__== '__main__':
    print(main())