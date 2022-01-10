from django.views.generic import TemplateView, ListView, DetailView
from .models import Team, Teamstats2021, Player


class Team2021View(ListView):
    template_name = "team.html"
    model = Team

class TeamIntro2021View(DetailView):
    template_name = "ti.html"
    model = Team
    context_object_name = 'teams'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context["pri"] = self.kwargs['pk']

        return context

class TeamBatt2021View(DetailView):
    template_name = "teamstats.html"
    model = Team
    context_object_name = 'teams'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('teamstats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す
        context["sit"] = "全球"
        context["num"] = 0

        return context

class TeamPit2021View(TemplateView):
    template_name = "stats.html"

class TeamPlayerBatt2021View(DetailView):
    template_name = "teambp.html"
    model = Team
    context_object_name = 'teams'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('TeamPlayer')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # はじめに継承元のメソッドを呼び出す
        context["pri"] = self.kwargs['pk']

        return context

class TeamPlayerPit2021View(TemplateView):
    template_name = "pit.html"



