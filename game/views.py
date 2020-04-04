from django.shortcuts import render
from django.http import HttpResponse
from game.models import *
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from game.rankapi import *
import datetime 
import collections
from operator import itemgetter
from django.forms import ModelForm
from game.filter import *
from django_filters.views import FilterView



class TeamCreateView(CreateView):
    model = Team
    fields = ['name']
    template_name = 'game/team/team-create.html'
    sucess_url = reverse_lazy('tournament-detail')

    def form_valid(self, form):
        form.instance.tournament = Tournament.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('tournament-detail', kwargs={'pk': self.object.tournament.pk})

class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'game/team/team-delete.html'
    context_object_name = 'teams'   
    sucess_url = reverse_lazy('tournament-detail')
    pk_url_kwarg = 'pk2'

    def get_success_url(self, **kwargs):
        return reverse('tournament-detail', kwargs={'pk': self.object.tournament.pk})

class TeamUpdateView(UpdateView):
    model = Team
    template_name = 'game/team/team-players.html'
    context_object_name = 'teams'   
    sucess_url = reverse_lazy('tournament-detail')
    pk_url_kwarg = 'pk2'
    fields = ['player1', 'player2', 'player3', 'player4', 'player5', 'player6', 'player7', 'player8', 'player9', 'player10']

    def get_success_url(self, **kwargs):
        return reverse('tournament-detail', kwargs={'pk': self.object.tournament.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)

        player1score = PlayerScore.objects.filter(playerScoreDate__year=datetime.datetime.now().year, playerScoreDate__week=datetime.datetime.now().isocalendar()[1], rank__gte=1,rank__lte=10).order_by('rank').values_list('player', flat=True)
        player1 = Player.objects.filter(id__in = player1score)

        player2score = PlayerScore.objects.filter(playerScoreDate__year=datetime.datetime.now().year, playerScoreDate__week=datetime.datetime.now().isocalendar()[1], rank__gte=11,rank__lte=20).order_by('rank').values_list('player', flat=True)
        player2 = Player.objects.filter(id__in = player2score)

        player3score = PlayerScore.objects.filter(playerScoreDate__year=datetime.datetime.now().year, playerScoreDate__week=datetime.datetime.now().isocalendar()[1], rank__gte=21,rank__lte=30).order_by('rank').values_list('player', flat=True)
        player3 = Player.objects.filter(id__in = player3score)

        player4score = PlayerScore.objects.filter(playerScoreDate__year=datetime.datetime.now().year, playerScoreDate__week=datetime.datetime.now().isocalendar()[1], rank__gte=31,rank__lte=40).order_by('rank').values_list('player', flat=True)
        player4 = Player.objects.filter(id__in = player4score)

        player5score = PlayerScore.objects.filter(playerScoreDate__year=datetime.datetime.now().year, playerScoreDate__week=datetime.datetime.now().isocalendar()[1], rank__gte=41,rank__lte=50).order_by('rank').values_list('player', flat=True)
        player5 = Player.objects.filter(id__in = player5score)

        player6score = PlayerScore.objects.filter(playerScoreDate__year=datetime.datetime.now().year, playerScoreDate__week=datetime.datetime.now().isocalendar()[1], rank__gte=51,rank__lte=60).order_by('rank').values_list('player', flat=True)
        player6 = Player.objects.filter(id__in = player6score)

        player7score = PlayerScore.objects.filter(playerScoreDate__year=datetime.datetime.now().year, playerScoreDate__week=datetime.datetime.now().isocalendar()[1], rank__gte=61,rank__lte=70).order_by('rank').values_list('player', flat=True)
        player7 = Player.objects.filter(id__in = player7score)

        player8score = PlayerScore.objects.filter(playerScoreDate__year=datetime.datetime.now().year, playerScoreDate__week=datetime.datetime.now().isocalendar()[1], rank__gte=71,rank__lte=80).order_by('rank').values_list('player', flat=True)
        player8 = Player.objects.filter(id__in = player8score)

        player9score = PlayerScore.objects.filter(playerScoreDate__year=datetime.datetime.now().year, playerScoreDate__week=datetime.datetime.now().isocalendar()[1], rank__gte=81,rank__lte=90).order_by('rank').values_list('player', flat=True)
        player9 = Player.objects.filter(id__in = player9score)

        player10score = PlayerScore.objects.filter(playerScoreDate__year=datetime.datetime.now().year, playerScoreDate__week=datetime.datetime.now().isocalendar()[1], rank__gte=91,rank__lte=100).order_by('rank').values_list('player', flat=True)
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

class TournamentListView(ListView):
    model = Tournament
    template_name = 'game/home.html'
    context_object_name = 'tournaments'
    ordering = ['-date_created_tournament']

class TournamentDetailView(FilterView):
    template_name = 'game/tournament/tournament-detail.html'
    model = PlayerScore
    filterset_class = PlayerScoreFilter
    
    def getPlayerRank(self, player, year, week):
        if(PlayerScore.objects.filter(player=player, playerScoreDate__year=year, playerScoreDate__week=week).exists()):
            return PlayerScore.objects.get(player=player, playerScoreDate__year=year, playerScoreDate__week=week).rank
        else:
            return 0

    def getPlayerRankChange(self, player, year, week):
        year_last_rank = year
        week_last_rank = week - 1
        rank_change = ""
        # Check if in between 2 years
        if(week==1):
            year_last_rank = year - 1
            week_last_rank = 52
        playerRank = self.getPlayerRank(player, year, week)
        playerRank_last_week = self.getPlayerRank(player, year_last_rank, week_last_rank)
        if(playerRank_last_week != 0):
            rank_change = playerRank_last_week - playerRank
            if(rank_change>0):
                rank_change = "↗ " + str(rank_change)
            else:
                rank_change = "↘ " + str(abs(rank_change))
        return rank_change

    def getPlayerListFromTeamObject(self, team): 
        return [team.player1, team.player2, team.player3, team.player4, team.player5, team.player6, team.player7, team.player8, team.player9, team.player10]

    def getTeamScore(self, team, year, week):
        players = self.getPlayerListFromTeamObject(team)
        score=0
        for player in players :
            score += self.getPlayerRank(player, year, week)
        return score 

    def getTeamPlayerRankList(self, team, year, week):
        player_rank_list = list()
        for player in self.getPlayerListFromTeamObject(team):
            player_rank_list.append(self.getPlayerRank(player, year, week))
        return player_rank_list

    def getTeamPlayerRankChangeList(self, team, year, week):
        player_rank_change_list = list()
        for player in self.getPlayerListFromTeamObject(team):
            player_rank_change_list.append(self.getPlayerRankChange(player, year, week))
        return player_rank_change_list
        
    def getTeamsMptScoreList(self, year, week): 
        teams = Team.objects.filter(tournament=self.kwargs['pk'])
        teams_mpt_score_set = list()
        for team in teams :
            teams_mpt_score_set.append([team, self.getTeamScore(team, year, week), self.getTeamPlayerRankList(team, year, week) , self.getTeamPlayerRankChangeList(team, year, week)])
        teams_mpt_score_set_sorted = sorted(teams_mpt_score_set, key=itemgetter(1))
        return teams_mpt_score_set_sorted
            
    def get_context_data(self, **kwargs):
        ctx = super(TournamentDetailView, self).get_context_data(**kwargs)
        filtered_year = ctx['filter'].qs.first().playerScoreDate.year
        filtered_week = ctx['filter'].qs.first().playerScoreDate.week
        ctx['teams_mpt_score_set'] = self.getTeamsMptScoreList(filtered_year, filtered_week)
        ctx['tournament'] = Tournament.objects.get(id=self.kwargs['pk'])
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
    def get_context_data(self, **kwargs):
        ctx = super(PlayerListView, self).get_context_data(**kwargs)
        ctx['actualPlayerScores'] = PlayerScore.objects.filter(playerScoreDate__year=datetime.datetime.now().year, playerScoreDate__week=datetime.datetime.now().isocalendar()[1])
        return ctx
    
    api_tennis_uri = "api.sportradar.us"
    REST_method = "GET"
    resource = "/tennis-t2/en/players/rankings.json?api_key=bxrj5yreuyd9r4yy8afae3mb"
    
    api_response = api_tennis_connection(api_tennis_uri, REST_method, resource)
    api_data_to_player_model(api_response) 

