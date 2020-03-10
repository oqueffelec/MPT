from django.shortcuts import render
from django.http import HttpResponse
from game.models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from game.rankapi import *
import datetime 
import collections
from operator import itemgetter

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

        player1score = PlayerScore.objects.filter(year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1], rank__gte=1,rank__lte=11).order_by('rank')
        player1 = Player.objects.filter(id__in = player1score)

        player2score = PlayerScore.objects.filter(year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1], rank__gte=12,rank__lte=21).order_by('rank')
        player2 = Player.objects.filter(id__in = player2score)

        player3score = PlayerScore.objects.filter(year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1], rank__gte=22,rank__lte=31).order_by('rank')
        player3 = Player.objects.filter(id__in = player3score)

        player4score = PlayerScore.objects.filter(year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1], rank__gte=32,rank__lte=41).order_by('rank')
        player4 = Player.objects.filter(id__in = player4score)

        player5score = PlayerScore.objects.filter(year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1], rank__gte=42,rank__lte=51).order_by('rank')
        player5 = Player.objects.filter(id__in = player5score)

        player6score = PlayerScore.objects.filter(year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1], rank__gte=52,rank__lte=61).order_by('rank')
        player6 = Player.objects.filter(id__in = player6score)

        player7score = PlayerScore.objects.filter(year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1], rank__gte=62,rank__lte=71).order_by('rank')
        player7 = Player.objects.filter(id__in = player7score)

        player8score = PlayerScore.objects.filter(year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1], rank__gte=72,rank__lte=81).order_by('rank')
        player8 = Player.objects.filter(id__in = player8score)

        player9score = PlayerScore.objects.filter(year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1], rank__gte=82,rank__lte=91).order_by('rank')
        player9 = Player.objects.filter(id__in = player9score)

        player10score = PlayerScore.objects.filter(year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1], rank__gte=92,rank__lte=101).order_by('rank')
        player10 = Player.objects.filter(id__in = player10score)

        form.fields['player1'].queryset = player1
        form.fields['player2'].queryset = player2
        form.fields['player3'].queryset = player3
        form.fields['player4'].queryset = player4
        form.fields['player5'].queryset = player5
        form.fields['player6'].queryset = player6
        form.fields['player7'].queryset = player7
        form.fields['player8'].queryset = player8
        form.fields['player9'].queryset = player9
        form.fields['player10'].queryset = player10
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
    
    def getActualPlayerRank(self, player):
        if(PlayerScore.objects.filter(player=player).exists()):
            return PlayerScore.objects.get(player=player, year=datetime.datetime.now().year, week=datetime.datetime.now().isocalendar()[1]).rank
        else:
            return 0

    def getTeamsMptScoreDict(self): 
        teams = Team.objects.filter(tournament=self.kwargs['pk'])
        teams_mpt_score_set = list()
        for team in teams :
            teams_mpt_score_set.append([team, self.getActualPlayerRank(team.player1) + self.getActualPlayerRank(team.player2) + self.getActualPlayerRank(team.player3) + self.getActualPlayerRank(team.player4) + self.getActualPlayerRank(team.player5) + self.getActualPlayerRank(team.player6) + self.getActualPlayerRank(team.player7) + self.getActualPlayerRank(team.player8) + self.getActualPlayerRank(team.player9) + self.getActualPlayerRank(team.player10), [self.getActualPlayerRank(team.player1), self.getActualPlayerRank(team.player2), self.getActualPlayerRank(team.player3), self.getActualPlayerRank(team.player4), self.getActualPlayerRank(team.player5), self.getActualPlayerRank(team.player6), self.getActualPlayerRank(team.player7), self.getActualPlayerRank(team.player8), self.getActualPlayerRank(team.player9), self.getActualPlayerRank(team.player10)]])
        teams_mpt_score_set_sorted = sorted(teams_mpt_score_set, key=itemgetter(1))
        return teams_mpt_score_set_sorted

    def get_context_data(self, **kwargs):
        ctx = super(TournamentDetailView, self).get_context_data(**kwargs)
        print(self.getTeamsMptScoreDict())
        ctx['teams_mpt_score_set'] = self.getTeamsMptScoreDict()
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
    model = PlayerScore
    template_name = 'game/player/player-ranking.html'
    context_object_name = 'playerScores'
    ordering = ['rank'] 
    
    api_tennis_uri = "api.sportradar.us"
    REST_method = "GET"
    resource = "/tennis-t2/en/players/rankings.json?api_key=983nwtatskua4b54gawven3n"
    api_response = api_tennis_connection(api_tennis_uri, REST_method, resource)
    api_data_to_player_model(api_response) 

