from django.views.generic import TemplateView, ListView
from .models import Player, Stats2021

class Player2021View(ListView):
    template_name = "2021/player/player.html"
    model = Player

class PlayerSl2021View(TemplateView):
    template_name = "2021/player/playerstats.html"
    model = Player

class PlayerPl2021View(TemplateView):
    template_name = "2021/player/playerstats.html"
    model = Player


