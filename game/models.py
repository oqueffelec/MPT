from django.db import models

'''class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    nationality = models.TextField()
    age = models.IntegerField()
'''
class Tournament(models.Model):
    name = models.TextField()
    #user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

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




