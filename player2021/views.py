from django.views.generic import TemplateView, ListView
from .models import Player, Stats2021

class Player2021View(ListView):
    template_name = "player.html"
    model = Player

class PlayerSl2021View(TemplateView):
    template_name = "playerstats.html"
    model = Player

class PlayerPl2021View(TemplateView):
    template_name = "playerstats.html"
    model = Player

class PlayerBatt2021View(TemplateView):
    template_name = "playerstats.html"
    model = Player

class PlayerPit2021View(TemplateView):
    template_name = "playerstats.html"
    model = Player
