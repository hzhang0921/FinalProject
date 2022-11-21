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
    pprint.pprint(data)
    return data[0]

def get_match_stats(match_id):
    url = 'https://americas.api.riotgames.com/lol/match/v5/matches/' + match_id + '?api_key=' + RIOTAPI
    with urllib.request.urlopen(url) as f:
        repsonse_text = f.read().decode('utf-8')
        data = json.loads(repsonse_text)
    pprint.pprint(data)
    
def main():
    
   # get_puuid('SchtankyLeg','PANTS')
    #get_matchid(get_puuid('SchtankyLeg','PANTS'))
    get_match_stats(get_matchid(get_puuid('QuickPlatinum','NA1')))



if __name__== '__main__':
    print(main())