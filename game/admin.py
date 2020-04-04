from django.contrib import admin
from .models import Tournament, Player, PlayerScore, Team, PlayerScoreDate
# Register your models here.

admin.site.register(Tournament)
admin.site.register(Player)
admin.site.register(PlayerScore)
admin.site.register(Team)
admin.site.register(PlayerScoreDate)
