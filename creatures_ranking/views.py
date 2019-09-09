from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Count

from .forms import CreatureForm, RegisterForm, LoginForm, OrderForm
from .models import Creature, Castle, Votes
# Create your views here.
from django.views import View
from django.contrib.auth.models import User


class BaseView(View):
    def get(self, request):
        return render(request, '__base__.html')


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
        creature = Creature.objects.get(id=id)
        form = CreatureForm(instance=creature)
        return render(request, 'creature_form.html', {'form': form})

    def post(self, request, id):
        creature = Creature.objects.get(id=id)
        form = CreatureForm(request.POST, instance=creature)
        if form.is_valid():
            form.save()
            monster_id = id
            return HttpResponseRedirect(f'/creature_details/{monster_id}')
        else:
            invalid_monster_credentials_message = 'Invalid data. Correct it!'
            return render(request, 'creature_form.html',
                          {'form': form, 'invalid_monster_credentials_message': invalid_monster_credentials_message})


class CreatureRanking(View):
    def get(self, request):
        form = OrderForm()

        message = 'Ordered by fight value'
        ordered_rank = Creature.objects.order_by('-fight_value')
        general_rank = Creature.objects.order_by('-number_of_votes', '-fight_value')
        if request.user.is_authenticated:
            d_user_rank = Votes.objects.filter(user=request.user) \
                .values('vote_plus').annotate(Count('vote_plus'))
            user_rank = []
            for rank in d_user_rank:
                c = Creature.objects.get(id=rank['vote_plus'])
                c.number_of_votes = rank['vote_plus__count']
                user_rank.append(c)

            user_rank = sorted(user_rank, key=lambda o: o.number_of_votes, reverse=True)
        else:
            user_rank = []
        return render(request, 'creature_ranking.html',
                      {'ordered_rank': ordered_rank, 'general_rank': general_rank, 'form': form, 'message': message,
                       'user_rank': user_rank})

    def post(self, request):
        form = OrderForm(request.POST)
        order = 'fight_value'
        if form.is_valid():
            if form.cleaned_data['order'] == 'name':
                order = form.cleaned_data['order']
                message = f'Order by: {order}'
            else:
                order = f"-{form.cleaned_data['order']}"
                message = f'Order by: {order[1:]}'
        ordered_rank = Creature.objects.order_by(order)
        general_rank = Creature.objects.order_by('-number_of_votes', '-fight_value')
        if request.user.is_authenticated:
            d_user_rank = Votes.objects.filter(user=request.user) \
                .values('vote_plus').annotate(Count('vote_plus'))
            user_rank = []
            for rank in d_user_rank:
                c = Creature.objects.get(id=rank['vote_plus'])
                c.number_of_votes = rank['vote_plus__count']
                user_rank.append(c)

            user_rank = sorted(user_rank, key=lambda o: o.number_of_votes, reverse=True)
        else:
            user_rank = []
        form = OrderForm()
        return render(request, 'creature_ranking.html',
                      {'ordered_rank': ordered_rank, 'general_rank': general_rank, 'form': form, 'message': message,
                       'user_rank': user_rank})


class Voting(View):

    def get(self, request):
        winner = request.GET.get('winner')
        looser = request.GET.get('looser')
        if winner is None or looser is None:
            random_creatures = Creature.objects.order_by('?')
            creature1 = random_creatures[0]
            creature2 = random_creatures[1]
            return render(request, 'voting.html', {'creature1': creature1, 'creature2': creature2})
        else:
            user = request.user
            win_unit = Creature.objects.get(name=winner)
            los_unit = Creature.objects.get(name=looser)
            vote = Votes.objects.create(user=user, vote_plus=win_unit, vote_minus=los_unit)
            win_unit.number_of_votes += 1
            win_unit.save()
            return HttpResponseRedirect('/voting')


class LoginForms(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login_form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, '__base__.html', )
            else:
                invalid_credentials_message = 'Invalid credentials!'
                return render(request, 'login_form.html', {'form': form, 'message': invalid_credentials_message})
        else:
            return render(request, 'login_form.html', {'form': form})


class RegisterForms(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register_form.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            email = form.cleaned_data['Email']
            User.objects.create_user(username=username, password=password, email=email)
            return render(request, '__base__.html')
        return render(request, 'register_form.html', {'form': form})


class LogoutForms(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
