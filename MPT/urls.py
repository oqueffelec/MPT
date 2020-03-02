"""MPT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from game import views
from game.views import TeamCreateView, TournamentListView, TournamentDetailView, TournamentCreateView, TournamentDeleteView, TournamentTeamsListView, TeamDeleteView, PlayerListView, TeamUpdateView
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tournament/<int:pk>/team/new', TeamCreateView.as_view(), name='team-create'),
    path('tournament/<int:pk>/team/<int:pk2>/update', TeamUpdateView.as_view(), name='team-players'),
    path('players/', PlayerListView.as_view(), name='player-ranking'),
    path('tournament/<int:pk>/', TournamentDetailView.as_view(), name='tournament-detail'),
    path('tournament/<int:pk>/teams', TournamentTeamsListView.as_view(), name='tournament-teams'),
    path('tournament/new/', TournamentCreateView.as_view(), name='tournament-create'),
    path('tournament/<int:pk>/delete', TournamentDeleteView.as_view(success_url=reverse_lazy('home')), name='tournament-delete'),
    path('tournament/<int:pk>/teams/<int:pk2>/delete', TeamDeleteView.as_view(success_url=reverse_lazy('home')), name='team-delete'),
    path('', TournamentListView.as_view(), name='home'),
]
