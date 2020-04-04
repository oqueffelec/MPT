from django.db import models
from django.utils import timezone
from django.urls import reverse
import datetime

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    date_created_tournament = models.DateTimeField(default=timezone.now, verbose_name="date_created_tournament")
    description = models.TextField()

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
        return str(PlayerScore.objects.get(player=self, playerScoreDate__year=datetime.datetime.now().year, playerScoreDate__week=datetime.datetime.now().isocalendar()[1])) + ' ' + self.first_name + ' ' + self.last_name + ' -- ' + self.nationality 

    def playerWithoutRank(self): 
        return self.first_name + ' ' + self.last_name + ' -- ' + self.nationality 
        
class Team(models.Model):
    name = models.CharField(max_length=100)
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
    rank = models.IntegerField()
    atp_points = models.IntegerField()
    playerScoreDate = models.ForeignKey('PlayerScoreDate', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.rank)

class PlayerScoreDate(models.Model):
    year = models.IntegerField()
    week = models.IntegerField()
    date_created_playerScoreDate = models.DateTimeField(default=timezone.now, verbose_name="date_created_playerScore",  blank=True, null=True)

    def __str__(self):
        return "Semaine : " + str(self.week) + "   Année : " + str(self.year)
