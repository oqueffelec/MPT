import django_filters
from game.models import *
from django import forms


class PlayerScoreFilter(django_filters.FilterSet):
    class Meta:
        model = PlayerScore
        fields = ['playerScoreDate']

