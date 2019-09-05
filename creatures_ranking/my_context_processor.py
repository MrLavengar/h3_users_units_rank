from .models import Creature


def creature_list_ctx(request):
    creature_list = {'creature_list': Creature.objects.all().order_by('-fight_value')}
    return creature_list
