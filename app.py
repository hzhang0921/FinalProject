from flask import Flask
from flask import redirect
import requests
from requests.exceptions import HTTPError
from workspace import get_puuid
from flask import request
from flask import render_template
from workspace import get_matchid
from workspace import get_match_stats
from workspace import get_player_baitPings
from workspace import get_players
from workspace import get_match_id
from workspace import get_player_deaths
from workspace import get_player_kills
from workspace import get_player_assists
from workspace import get_player_visionScore
from workspace import get_player_teamPosition
from workspace import get_player_totaldamage
from workspace import get_player_championName
from workspace import get_player_ObejctiveDamage
from workspace import get_player_TurretDamage
from workspace import get_player_goldEarned
from workspace import get_player_pinkWards
from workspace import get_player_TotalDamagetoChampions
from workspace import get_player_CreepScore
from workspace import get_player_timeSpentDead
from workspace import get_player_turretTakedowns

#initialize flask
app = Flask(__name__)
#create the index page
@app.route('/')
def index():
    #send index to form.html template
    return render_template('form.html')
#create page that displays a users match history
@app.route('/matchpage/', methods = ["POST"])
def matchpage():
    #obtain data from form.html
    form_data = request.form
    #utilize try to account for error exceptions 
    try:
        #obtain information from form from immutable dict to string
        summonername = form_data.getlist('Summoner Name')[0]
        tagline = form_data.getlist('Tagline')[0]
        #obtain puuid from get_puuid function
        puuid = get_puuid(summonername,tagline)
        #obtian match id from puuid using get_matchid function
        match_id = get_matchid(puuid)
        #put each match id from list into seperate variables
        match1 = match_id[0]
        match2 = match_id[1]
        match3 = match_id[2]
        match4 = match_id[3]
        match5 = match_id[4]
        #send variables to matchpage.html to create match history page
        return render_template('matchpage.html', match1= match1, match2=match2, match3=match3, match4=match4, match5 =match5 )

    #in the case an error occurs
    except Exception as e:
    #     #if an error occurs, redirect the user to /error, showing the error.html template
         return redirect(('/error'))
#creation of an error page
@app.route('/error')
def error():
    #return error.html template
    return render_template('error.html')

#create app route to display each player in a set match
@app.route('/match1', methods = ["POST"])
def match1():
    #obtain data from matchpage form
    form_data = request.form
    #put matchpage data into useable format
    dictmatch_id = form_data.keys()
    for value in dictmatch_id:
        #create match id variable
        matchid=value
    #get the data from match using get_match_stats method with input id 
    matchdata = get_match_stats(matchid)
    #get dictionary of players using get_players
    players = get_players(matchdata)
    #put each individual player's summoner name into seperate variables
    player1 = players[0][0]
    player2 = players[1][0]
    player3 = players[2][0]
    player4 = players[3][0]
    player5 = players[4][0]
    player6 = players[5][0]
    player7 = players[6][0]
    player8 = players[7][0]
    player9 = players[8][0]
    player10 = players[9][0]
    #return template to matchplayers.html, send in each player's summoner name in variables
    return render_template('matchplayers.html', player1 = player1, player2 = player2, player3 = player3, player4 = player4, player5 = player5,
    player6= player6, player7= player7, player8= player8, player9 = player9, player10 =player10, matchid = matchid)
    #matchid = 
#create app route from each player's stats
@app.route('/playerstats', methods =['POST'])
def matchstats():
    #obtain data
    form_data = request.form
    #translate form data into useable format 
    for value in form_data:
        placeholder = value
    newlist = placeholder.split(',')
    matchid = newlist[0]
    summonername =newlist[1]
    #create variables using functions from workspace.py
    #variables will be passed to template in the future
    matchdata = get_match_stats(matchid)
    baitpings = get_player_baitPings(matchdata,summonername)
    kills = get_player_kills(matchdata,summonername)
    deaths = get_player_deaths(matchdata,summonername)
    assists = get_player_assists(matchdata,summonername)
    visionScore = get_player_visionScore(matchdata,summonername)
    teamPosition = get_player_teamPosition(matchdata,summonername)
    totaldamage = get_player_totaldamage(matchdata,summonername)
    championName = get_player_championName(matchdata,summonername)
    ObjectiveDamage = get_player_ObejctiveDamage(matchdata,summonername)
    TurretDamage = get_player_TurretDamage(matchdata,summonername)
    goldEarned = get_player_goldEarned(matchdata,summonername)
    pinkWards = get_player_pinkWards(matchdata,summonername)
    TotalDamagetoChampions = get_player_TotalDamagetoChampions(matchdata,summonername)
    CreepScore = get_player_CreepScore(matchdata,summonername)
    timeSpentDead = get_player_timeSpentDead(matchdata,summonername)
    turretTakedowns = get_player_turretTakedowns(matchdata,summonername)
    baitPings = get_player_baitPings(matchdata,summonername)

    #create the playerstats template which displays a player's stats for a game. Send each variable intialized above through this form
    return render_template('playerstats.html', baitpings=baitpings,summonername=summonername,kills=kills,deaths=deaths, assists=assists, visionScore=visionScore, 
        teamPosition =teamPosition, totaldamage= totaldamage, championName= championName, ObjectiveDamage = ObjectiveDamage, TurretDamage = TurretDamage, goldEarned = goldEarned,
        pinkWards=pinkWards, TotalDamagetoChampions = TotalDamagetoChampions, CreepScore= CreepScore, timeSpentDead = timeSpentDead, turretTakedowns = turretTakedowns, baitPings=baitPings)
#run app
if __name__ == '__main__':
    app.run(debug=True)    