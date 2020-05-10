import http.client
import json 
import pandas as pd
import sys     
from game.models import *
import datetime 
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):  
    api_tennis_uri = "api.sportradar.us"
    REST_method = "GET"
    resource = "/tennis-t2/en/players/rankings.json?api_key=9uhz8mcja8pb5krnez2nr8t8"

    def api_tennis_connection(self, api_uri, REST_method, resource):
        conn = http.client.HTTPSConnection(api_uri)
        conn.request(REST_method, resource)
        res = conn.getresponse()
        return json.loads(res.read())

    def getOrCreateCurrentPlayerScoreDate(self, player):
        # Check if current date already exists in PlayerScoreDate model
        if(PlayerScoreDate.objects.filter(week = datetime.datetime.now().isocalendar()[1]).exists() and PlayerScoreDate.objects.filter(year = datetime.datetime.now().year).exists()):
            playerScoreDate = PlayerScoreDate.objects.get(year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1])
        else:
            playerScoreDate = PlayerScoreDate(year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1], date_created_playerScoreDate=datetime.datetime.now())
            playerScoreDate.save()
        return playerScoreDate
        

    def api_data_to_player_model(self, api_response):
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
                        if(not(playerScore.filter(playerScoreDate__week = datetime.datetime.now().isocalendar()[1]).exists() or not(playerScore.filter(playerScoreDate__year = datetime.datetime.now().year).exists())) and datetime.datetime.now().hour > 10):
                            playerScoreDate = self.getOrCreateCurrentPlayerScoreDate(player)
                            PlayerScore(player=player, playerScoreDate=playerScoreDate, rank=item['rank'], atp_points=item['points']).save()
                    else:
                        playerScoreDate = self.getOrCreateCurrentPlayerScoreDate(player)
                        PlayerScore(player=player, playerScoreDate=playerScoreDate, rank=item['rank'], atp_points=item['points']).save()
                else:
                    playerScoreDate = self.getOrCreateCurrentPlayerScoreDate(player)
                    PlayerScore(player=player, playerScoreDate=playerScoreDate, rank=item['rank'], atp_points=item['points']).save()
            else:
                player = Player(first_name=item['player']['name'].split(', ')[1], last_name=item['player']['name'].split(', ')[0], nationality=item['player']['nationality'])
                player.save()
                playerScoreDate = self.getOrCreateCurrentPlayerScoreDate(player)
                PlayerScore(player=player, playerScoreDate=playerScoreDate, rank=item['rank'], atp_points=item['points']).save()
        return

    def handle(self, *args, **options):
        api_response = self.api_tennis_connection(self.api_tennis_uri, self.REST_method, self.resource)
        self.api_data_to_player_model(api_response)
        return 
