"""coderslab URL Configuration

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

from exercises_app.views import show_articles, show_bands
from football.views import league_table, show_games_played, add_game, modify_team
from ui_app.views import show_pretty_ui

urlpatterns = [
    path("admin/", admin.site.urls),
    path("articles/", show_articles),
    path("show-band/<int:band_id>/", show_bands),
    path("table/", league_table),
    path("games_played/<int:team_id>/", show_games_played),
    path("add-game/", add_game),
    path("modify-team/<int:team_id>/", modify_team),
    path("ui/", show_pretty_ui)
]
