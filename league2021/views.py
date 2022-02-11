from django.views.generic import DetailView, ListView, TemplateView
from .models import League, Leaguestats2021, Statsrank2021


class league2021View(ListView):
    template_name = "league/league.html"
    model = League

class leagueIntro2021View(DetailView):
    template_name = "league/li.html"
    model = League
    context_object_name = 'leagues'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context["pri"] = self.kwargs['pk']

        return context



class leaguePlayerBatt2021View(ListView):
    template_name = "league/leaguebp.html"
    model = Statsrank2021
    context_object_name = 'leagues'

    def get_queryset(self):
        return Statsrank2021.objects.filter(pa__gt=100).order_by('-avg')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す
        context["pri"] = self.kwargs['pk']

        return context

class leaguePlayerPit2021View(TemplateView):
    template_name = "league/pit.html"