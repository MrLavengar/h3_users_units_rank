from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CreatureForm
from .models import Creature, Castle
# Create your views here.
from django.views import View


class CreatureDetails(View):
    def get(self, request, id):
        creature = Creature.objects.get(id=id)
        return render(request, 'creature_details.html', {'creature': creature})


class CastleCreatureList(View):
    def get(self, request, castle):
        castle = Castle.objects.get(castle_name=castle)
        creatures_list = Creature.objects.filter(castle_name=castle)
        return render(request, 'castle_creature_list.html', {'creatures_list': creatures_list, 'castle': castle})


class EditCreatureForm(View):
    def get(self, request, id):
        # creature = Creature.objects.get(id=id)
        # creature_data =
        form = CreatureForm()
        return render(request, 'creature_form.html', {'form': form})

    def post(self, request):
        form = CreatureForm(request.POST)
        if form.is_valid():
            new_creature = form.save()
        return HttpResponseRedirect(f'/creature_details/{new_creature.id}')
