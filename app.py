from flask import Flask
from flask import redirect
from workspace import get_puuid
from flask import request
from flask import render_template
from workspace import get_matchid
from workspace import get_match_stats
from workspace import get_bait_pings
from workspace import get_players
from workspace import get_player_stats
app = Flask(__name__)

@app.route('/')
def index():

    return render_template('form.html')

@app.route('/matchpage/', methods = ["POST"])
def matchpage():
    form_data = request.form
    #print(form_data)
    # print("joen")
    # print(form_data)
    # print(form_data.getlist('Summoner Name')[0])
    # print('keo')
    #print(form_data[1])
    #return render_template('matchpage.html')
        #access the balues from the form
    # for value in form_data.values():
    summonername = form_data.getlist('Summoner Name')[0]
    tagline = form_data.getlist('Tagline')[0]
    puuid = get_puuid(summonername,tagline)
    #return the template locaiton.html, send in variable sstop and wheelchair
    match_id = get_matchid(puuid)
    print(match_id)
    match1 = match_id[0]
    match2 = match_id[1]
    match3 = match_id[2]
    match4 = match_id[3]
    match5 = match_id[4]
    return render_template('matchpage.html', match1= match1, match2=match2, match3=match3, match4=match4, match5 =match5 )
    # try:
    #     #use the function find_stop_near from mbta_helper.py to find the MBTA stop from the value obtained from the form
    #     # stats = full_stats(value)
    #     #split the MBTA stop and wheelchair accessibility into distinct bariables
    #     summonername = form_data.getlist('Summoner Name')[0]
    #     tagline = form_data.getlist('Tagline')[0]
    #     #return the template locaiton.html, send in variable sstop and wheelchair
    #     match_id = get_matchid(summonername,tagline)
    #     print(match_id)
    #     return render_template('matchpage.html', summonername=summonername, tagline = tagline )
    # #in the case an error occurs
    # except (IndexError,TypeError):
    #     #if an index or type error occurs, redirect the user to /error, showing the error.html template
    #     return redirect(('/error'))


@app.route('/match1', methods = ["POST"])
def match1():
    form_data = request.form
    #print(form_data)
    dictmatch_id = form_data.keys()
    #print(dictmatch_id)
    for value in dictmatch_id:
        matchid=value
    #print(matchid)
    matchdata = get_match_stats(matchid)
    players = get_players(matchdata)
    player1 = str(players[0][0])
    player2 = players[1][0]
    player3 = players[2][0]
    player4 = players[3][0]
    player5 = players[4][0]
    player6 = players[5][0]
    player7 = players[6][0]
    player8 = players[7][0]
    player9 = players[8][0]
    player10 = players[9][0]

    return render_template('matchplayers.html', player1 = player1, player2 = player2, player3 = player3, player4 = player4, player5 = player5,
    player6= player6, player7= player7, player8= player8, player9 = player9, player10 =player10, matchid = matchid)
    #matchid = 

@app.route('/playerstats', methods =['POST'])
def matchstats():
    form_data = request.form
    for value in form_data:
        placeholder = value
    newlist = placeholder.split(',')
    matchid = newlist[0]
    summonername =newlist[1]
    matchdata = get_match_stats(matchid)
    baitpings = get_player_stats(matchdata,summonername)
    return render_template('playerstats.html', baitpings=baitpings,summonername=summonername)

if __name__ == '__main__':
    app.run(debug=True)    