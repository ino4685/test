from django.views.generic import DetailView
from .models import League, Leaguestats2021

tempurl = "2021/league/leaguestats.html"

class La2021View(DetailView):
    template_name = tempurl
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


class Lavr2021View(DetailView):
    template_name = tempurl
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

class Lavl2021View(DetailView):
    template_name = tempurl
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

class Lac2021View(DetailView):
    template_name = tempurl
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

class Las2021View(DetailView):
    template_name = tempurl
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

class Lavt2021View(DetailView):
    template_name = tempurl
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

class Lai2021View(DetailView):
    template_name = tempurl
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

class Lacount2021View(DetailView):
    template_name = tempurl
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

class Lacourse2021View(DetailView):
    template_name = tempurl
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

class Labn2021View(DetailView):
    template_name = tempurl
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

class Lap2021View(DetailView):
    template_name = tempurl
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

class Law2021View(DetailView):
    template_name = tempurl
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

class Labase2021View(DetailView):
    template_name = tempurl
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

class Lam2021View(DetailView):
    template_name = tempurl
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

class Laposi2021View(DetailView):
    template_name = tempurl
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