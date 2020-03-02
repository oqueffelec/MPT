import http.client
import json 
import pandas as pd
import sys     
from game.models import *


def api_tennis_connection(api_uri, REST_method, resource):
    conn = http.client.HTTPSConnection(api_uri)
    conn.request(REST_method, resource)
    res = conn.getresponse()
    return json.loads(res.read())

def api_data_to_player_model(api_response):
    atp_player_rankings = api_response["rankings"][1]["player_rankings"]
    for item in atp_player_rankings:
        if(Player.objects.filter(name=item['player']['name']).exists()):
            Player.objects.filter(name=item['player']['name']).update(rank=item['rank'], atp_points=item['points'])
        else:
            Player(name=item['player']['name'], nationality=item['player']['nationality'], rank=item['rank'], atp_points=item['points']).save()
