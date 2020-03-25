from django.db import models
from django.utils import timezone
from django.urls import reverse
import datetime

'''class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    nationality = models.TextField()
    age = models.IntegerField()
'''
class Tournament(models.Model):
    name = models.TextField()
    date_created_tournament = models.DateTimeField(default=timezone.now, verbose_name="date_created_tournament")
    description = models.TextField()
    #user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Player(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    nationality = models.TextField()
    date_created_player = models.DateTimeField(default=timezone.now, verbose_name="date_created_player")


    def __str__(self):
        return str(PlayerScore.objects.get(player=self, year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1])) + ' ' + self.first_name + ' ' + self.last_name + ' -- ' + self.nationality 

class Team(models.Model):
    name = models.TextField()
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE)
    
    player1 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player1_player', blank=True, null=True )
    player2 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player2_player', blank=True, null=True )
    player3 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player3_player', blank=True, null=True )
    player4 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player4_player', blank=True, null=True )
    player5 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player5_player', blank=True, null=True )
    player6 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player6_player', blank=True, null=True )
    player7 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player7_player', blank=True, null=True )
    player8 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player8_player', blank=True, null=True )
    player9 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player9_player', blank=True, null=True )
    player10 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player10_player', blank=True, null=True )
    date_created_team = models.DateTimeField(default=timezone.now, verbose_name="date_created_team")

    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')



class PlayerScore(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player', blank=True, null=True, default=1)
    year = models.IntegerField()
    week = models.IntegerField()
    rank = models.IntegerField()
    atp_points = models.IntegerField()
    date_created_playerScore = models.DateTimeField(default=timezone.now, verbose_name="date_created_playerScore")


    def __str__(self):
        return str(self.rank)




