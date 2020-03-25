import http.client
import json 
import pandas as pd
import sys     
from game.models import *
import datetime 


def api_tennis_connection(api_uri, REST_method, resource):
    conn = http.client.HTTPSConnection(api_uri)
    conn.request(REST_method, resource)
    res = conn.getresponse()
    return json.loads(res.read())

def api_data_to_player_model(api_response):
    atp_player_rankings = api_response["rankings"][1]["player_rankings"]
    for item in atp_player_rankings: 
        # Check if player already exists in our Player model
        if(Player.objects.filter(first_name=item['player']['name'].split(', ')[1], last_name=item['player']['name'].split(', ')[0]).exists()):
            player = Player.objects.get(first_name=item['player']['name'].split(', ')[1], last_name=item['player']['name'].split(', ')[0])
            # Check if PlayerScore Table is empty
            if(PlayerScore.objects.count() != 0):
                # Check if a score already exists in our PlayerScoreModel for that Player
                if(PlayerScore.objects.filter(player=player).count() > 0):
                    # Get queryset of ranks that already exists for that player
                    playerScore = PlayerScore.objects.filter(player=player)
                    # Create score for that player only if there is no score for current year and current week
                    if(not(playerScore.filter(week = datetime.datetime.now().isocalendar()[1]).exists() or not(playerScore.filter(year = datetime.datetime.now().year).exists())) and datetime.datetime.now().hour > 15):
                        PlayerScore(player=player, year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1], rank=item['rank'], atp_points=item['points']).save()
                else:
                    PlayerScore(player=player, year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1], rank=item['rank'], atp_points=item['points']).save()
            else:
                PlayerScore(player=player, year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1], rank=item['rank'], atp_points=item['points']).save()
        else:
            player = Player(first_name=item['player']['name'].split(', ')[1], last_name=item['player']['name'].split(', ')[0], nationality=item['player']['nationality'])
            player.save()
            PlayerScore(player=player, year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1], rank=item['rank'], atp_points=item['points']).save()

