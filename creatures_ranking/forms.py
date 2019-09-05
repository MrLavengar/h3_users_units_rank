from django import forms
from django.forms import ModelForm
from creatures_ranking.models import Creature


class CreatureForm(ModelForm):
    class Meta:
        model = Creature
        fields = '__all__'
