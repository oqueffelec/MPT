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
from django.contrib.auth import views as auth_views
from django.urls import path
from game import views
from game.views import TeamCreateView, TournamentListView, TournamentDetailView, TournamentCreateView, TournamentDeleteView, TeamDeleteView, PlayerListView, TeamUpdateView
from django.urls import reverse_lazy
from users import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
    path('tournament/<int:pk>/team/new', TeamCreateView.as_view(), name='team-create'),
    path('tournament/<int:pk>/team/<int:pk2>/update', TeamUpdateView.as_view(success_url=reverse_lazy('tournament-detail')), name='team-players'),
    path('players/', PlayerListView.as_view(), name='player-ranking'),
    path('tournament/<int:pk>/', TournamentDetailView.as_view(), name='tournament-detail'),
    path('tournament/new/', TournamentCreateView.as_view(), name='tournament-create'),
    path('tournament/<int:pk>/delete', TournamentDeleteView.as_view(success_url=reverse_lazy('home')), name='tournament-delete'),
    path('tournament/<int:pk>/teams/<int:pk2>/delete', TeamDeleteView.as_view(success_url=reverse_lazy('home')), name='team-delete'),
    path('', TournamentListView.as_view(), name='home'),
]
