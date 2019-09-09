"""h3_users_units_rank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from creatures_ranking.views import CreatureDetails, CastleCreatureList, EditCreatureForm, BaseView, CreatureRanking, \
    Voting,RegisterForms,LoginForms,LogoutForms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView.as_view(), name='base'),
    path('creature_details/<int:id>', CreatureDetails.as_view(), name='creature-details'),
    path('castle_creature_list/<str:castle>', CastleCreatureList.as_view(), name='castle-creature-list'),
    path('edit_creature/<int:id>', EditCreatureForm.as_view(), name='edit-creature'),
    path('creature_ranking/', CreatureRanking.as_view(), name='creature-ranking'),
    path('voting/', Voting.as_view(), name=''),
    path('register/', RegisterForms.as_view(), name=''),
    path('login/', LoginForms.as_view(), name=''),
    path('logout/', LogoutForms.as_view(), name=''),


]
