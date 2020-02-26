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
    #user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Team(models.Model):
    name = models.TextField()
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE)

class Player(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    nationality = models.TextField()
    age = models.IntegerField()
    rank = models.IntegerField()
    team = models.ForeignKey('Team', on_delete=models.CASCADE)




