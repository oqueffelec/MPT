from django.db import models
from django.utils import timezone
from django.urls import reverse

'''class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    nationality = models.TextField()
    age = models.IntegerField()
'''
class Tournament(models.Model):
    name = models.TextField()
    date_created = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
    description = models.TextField()
    #user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Team(models.Model):
    name = models.TextField()
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE)
    
    player1 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player1_player', blank=True, null=True, default=1)
    player2 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player2_player', blank=True, null=True, default=10)
    player3 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player3_player', blank=True, null=True, default=20)
    player4 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player4_player', blank=True, null=True, default=30)
    player5 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player5_player', blank=True, null=True, default=40)
    player6 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player6_player', blank=True, null=True, default=50)
    player7 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player7_player', blank=True, null=True, default=60)
    player8 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player8_player', blank=True, null=True, default=70)
    player9 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player9_player', blank=True, null=True, default=80)
    player10 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player10_player', blank=True, null=True, default=90)

    @property
    def mpt_score(self):
        return self.player1.rank + self.player2.rank + self.player3.rank + self.player4.rank + self.player5.rank + self.player6.rank + self.player7.rank + self.player8.rank + self.player9.rank + self.player10.rank 

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Player(models.Model):
    name = models.TextField()
    nationality = models.TextField()
    rank = models.IntegerField()
    atp_points = models.IntegerField()
    

    def __str__(self):
        return str(self.rank) + '   ' + self.name + '   ' + self.nationality + '   ' + str(self.atp_points)




