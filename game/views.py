from django.shortcuts import render
from django.http import HttpResponse
from game.models import *
# Create your views here.

def home(request):
    tournaments = Tournament.objects.all()
    return render(request, 'game/home.html', {'tournaments' : tournaments})

def tournament(request):
    return HttpResponse("""<h1> Creer ou rejoindre un tournoi </h1>""")

def team(request):
    return HttpResponse("""<h1>Creer son equipe</h1>""")

def player(request):
    return HttpResponse("""<h1> Selectionner un joueur de chaque top10</h1>""")
