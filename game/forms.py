from django import forms

class TournamentForm(forms.Form):
    name = forms.CharField(label='Nouveau Tournoi ', max_length=100)