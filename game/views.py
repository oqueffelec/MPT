from django.shortcuts import render
from django.http import HttpResponse
from game.models import *
from .forms import TournamentForm

def home(request):
    tournaments = Tournament.objects.all()
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid(): 
           tournament_name = form.cleaned_data['name']
           Tournament(name = tournament_name).save()
    else : 
        form = TournamentForm()
    return render(request, 'game/home.html', locals())

def tournament(request):
    return HttpResponse("""<h1> Creer ou rejoindre un tournoi </h1>""")

def team(request):
    return HttpResponse("""<h1>Creer son equipe</h1>""")

def player(request):
    return HttpResponse("""<h1> Selectionner un joueur de chaque top10</h1>""")
