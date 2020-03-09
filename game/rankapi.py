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
        if(Player.objects.filter(name=item['player']['name']).exists()):
            player = Player.objects.get(name=item['player']['name'])
            # Check if a score already exists in our PlayerScoreModel for that Player
            if(not(PlayerScore.DoesNotExist)):
                if(PlayerScore.objects.get(player=player).exists()):
                    playerScore = PlayerScore.objects.get(player=player)
                    # Create score for that player only if there is no score for current year and current week
                    if((not(playerScore.values_list('week', flat=True) == datetime.datetime.now().isocalendar()[1]) or not(playerScore.values_list('year', flat=True) == datetime.datetime.now().year)) and datetime.datetime.now().hour > 16):
                        PlayerScore(player=player, year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1], rank=item['rank'], atp_points=item['points']).save()
                else:
                    PlayerScore(player=player, year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1], rank=item['rank'], atp_points=item['points']).save()
        else:
            player = Player(name=item['player']['name'], nationality=item['player']['nationality'])
            player.save()
            PlayerScore(player=player, year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1], rank=item['rank'], atp_points=item['points']).save()

