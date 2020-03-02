from django.shortcuts import render
from django.http import HttpResponse
from game.models import *
from .forms import TournamentForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from game.rankapi import *



class TeamCreateView(CreateView):
    model = Team
    fields = ['name']
    template_name = 'game/team/team-create.html'

    def form_valid(self, form):
        form.instance.tournament = Tournament.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'game/team/team-delete.html'
    context_object_name = 'teams'   
    sucess_url = reverse_lazy('home')
    pk_url_kwarg = 'pk2'

class TeamUpdateView(UpdateView):
    model = Team
    template_name = 'game/team/team-players.html'
    context_object_name = 'teams'   
    sucess_url = reverse_lazy('home')
    pk_url_kwarg = 'pk2'
    fields = ['player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9', 'player10']

class TournamentTeamsListView(ListView):
    model = Team
    template_name = 'game/tournament/tournament-teams.html'
    context_object_name = 'teams'

    def get_queryset(self, *args, **kwargs):
        return Team.objects.filter(tournament=self.kwargs['pk'])

class TournamentListView(ListView):
    model = Tournament
    template_name = 'game/home.html'
    context_object_name = 'tournaments'
    ordering = ['-date_created']

class TournamentDetailView(DetailView):
    model = Tournament
    template_name = 'game/tournament/tournament-detail.html'
    context_object_name = 'tournaments'

class TournamentCreateView(CreateView):
    model = Tournament
    fields = ['name', 'description']
    template_name = 'game/tournament/tournament-create.html'

class TournamentDeleteView(DeleteView):
    model = Tournament
    template_name = 'game/tournament/tournament-delete.html'
    context_object_name = 'tournaments'
    fields = ['name']
    sucess_url = reverse_lazy('home')


class PlayerListView(ListView):
    
    api_tennis_uri = "api.sportradar.us"
    REST_method = "GET"
    resource = "/tennis-t2/en/players/rankings.json?api_key=rrynxp6dktf4z4qb4gh4rha2"
    api_response = api_tennis_connection(api_tennis_uri, REST_method, resource)
    top = api_data_to_player_model(api_response) 

    model = Player
    template_name = 'game/player/player-ranking.html'
    context_object_name = 'players'
    ordering = ['rank']

