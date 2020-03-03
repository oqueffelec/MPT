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
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['player1'].queryset = form.fields['player1'].queryset.filter(rank__lte=10).order_by('rank')
        form.fields['player2'].queryset = form.fields['player2'].queryset.filter(rank__gte=11,rank__lte=20).order_by('rank')
        form.fields['player3'].queryset = form.fields['player3'].queryset.filter(rank__gte=21,rank__lte=30).order_by('rank')
        form.fields['player4'].queryset = form.fields['player4'].queryset.filter(rank__gte=31,rank__lte=40).order_by('rank')
        form.fields['player5'].queryset = form.fields['player5'].queryset.filter(rank__gte=41,rank__lte=50).order_by('rank')
        form.fields['player6'].queryset = form.fields['player6'].queryset.filter(rank__gte=51,rank__lte=60).order_by('rank')
        form.fields['player7'].queryset = form.fields['player7'].queryset.filter(rank__gte=61,rank__lte=70).order_by('rank')
        form.fields['player8'].queryset = form.fields['player8'].queryset.filter(rank__gte=71,rank__lte=80).order_by('rank')
        form.fields['player9'].queryset = form.fields['player9'].queryset.filter(rank__gte=81,rank__lte=90).order_by('rank')
        form.fields['player10'].queryset = form.fields['player10'].queryset.filter(rank__gte=91,rank__lte=100).order_by('rank')
        return form

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
    

    def get_context_data(self, **kwargs):
        ctx = super(TournamentDetailView, self).get_context_data(**kwargs)
        ctx['teams'] = sorted(Team.objects.filter(tournament=self.kwargs['pk']), key=lambda team: team.mpt_score) 
        return ctx

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

