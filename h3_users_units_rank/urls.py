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

from creatures_ranking.views import BaseView, CreatureDetails, CastleCreatureList,EditCreatureForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView.as_view(), name='base-view'),
    path('creature_details/<int:id>', CreatureDetails.as_view(), name='base-view'),
    path('castle_creature_list/<str:castle>', CastleCreatureList.as_view(), name=''),
    path('creature_details/<int:id>', EditCreatureForm.as_view(), name=''),
]
