from django.views.generic import DetailView
from .models import League, Leaguestats2021P

class Lp2021View(DetailView):
    template_name = "league/leaguestatsP.html"
    model = League
    context_object_name = 'leagues'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('league')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context["sit"] = "全球"
        context["num"] = 0

        return context


class Lavrp2021View(DetailView):
    template_name = "league/leaguestatsP.html"
    model = League
    context_object_name = 'leagues'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('league')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "対右"
        context["num"] = 2
        return context

class Lavlp2021View(DetailView):
    template_name = "league/leaguestatsP.html"
    model = League
    context_object_name = 'leagues'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('league')
        return qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "対左"
        context["num"] = 3
        return context

class Lacp2021View(DetailView):
    template_name = "league/leaguestatsP.html"
    model = League
    context_object_name = 'leagues'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('league')
        return qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "得点圏"
        context["num"] = 1
        return context

class Lasp2021View(DetailView):
    template_name = "league/leaguestatsP.html"
    model = League
    context_object_name = 'leagues'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('league')
        return qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "球場別"
        context["num"] = 13
        return context

class Lavtp2021View(DetailView):
    template_name = "league/leaguestatsP.html"
    model = League
    context_object_name = 'leagues'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('league')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "対チーム別"
        context["num"] = 12
        return context

class Laip2021View(DetailView):
    template_name = "league/leaguestatsP.html"
    model = League
    context_object_name = 'leagues'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('league')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "イニング別"
        context["num"] = 4
        return context

class Lacountp2021View(DetailView):
    template_name = "league/leaguestatsP.html"
    model = League
    context_object_name = 'leagues'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('league')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "カウント別"
        context["num"] = 5
        return context

class Lacoursep2021View(DetailView):
    template_name = "league/leaguestatsP.html"
    model = League
    context_object_name = 'leagues'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('league')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "コース別"
        context["num"] = 6
        return context

class Labnp2021View(DetailView):
    template_name = "league/leaguestatsP.html"
    model = League
    context_object_name = 'leagues'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('league')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "打順別"
        context["num"] = 11
        return context

class Lapp2021View(DetailView):
    template_name = "league/leaguestatsP.html"
    model = League
    context_object_name = 'leagues'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('league')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "点差別"
        context["num"] = 10
        return context

class Lawp2021View(DetailView):
    template_name = "league/leaguestatsP.html"
    model = League
    context_object_name = 'leagues'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('league')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "曜日別"
        context["num"] = 9
        return context

class Labasep2021View(DetailView):
    template_name = "league/leaguestatsP.html"
    model = League
    context_object_name = 'leagues'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('league')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "塁別"
        context["num"] = 7
        return context

class Lamp2021View(DetailView):
    template_name = "league/leaguestatsP.html"
    model = League
    context_object_name = 'leagues'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('league')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "月別"
        context["num"] = 8
        return context

class Laposip2021View(DetailView):
    template_name = "league/leaguestatsP.html"
    model = League
    context_object_name = 'leagues'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('league')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "守備位置別"
        context["num"] = 13
        return context