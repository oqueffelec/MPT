from django.shortcuts import render
from django.http import HttpResponse
from game.models import *
from .forms import TournamentForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy

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
