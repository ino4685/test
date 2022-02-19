from django.views.generic import ListView, DetailView
from .models import Team, Teamstats2021

tempurl = "2021/team/teamstats.html"

class Tab2021View(DetailView):
    template_name = tempurl
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



class Tvr2021View(DetailView):
    template_name = tempurl
    model = Team
    context_object_name = 'teams'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('teamstats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "対右"
        context["num"] = 2
        return context

class Tvl2021View(DetailView):
    template_name = tempurl
    model = Team
    context_object_name = 'teams'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('teamstats')  # team -> playerの逆参照なので、related_nameを使用
        return qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "対左"
        context["num"] = 3
        return context

class Tc2021View(DetailView):
    template_name = tempurl
    model = Team
    context_object_name = 'teams'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('teamstats')  # team -> playerの逆参照なので、related_nameを使用
        return qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "得点圏"
        context["num"] = 1
        return context

class Ts2021View(DetailView):
    template_name = tempurl
    model = Team
    context_object_name = 'teams'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('teamstats')  # team -> playerの逆参照なので、related_nameを使用
        return qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "球場別"
        context["num"] = 13
        return context

class Tvt2021View(DetailView):
    template_name = tempurl
    model = Team
    context_object_name = 'teams'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('teamstats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "対チーム別"
        context["num"] = 12
        return context

class Ti2021View(DetailView):
    template_name = tempurl
    model = Team
    context_object_name = 'teams'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('teamstats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "イニング別"
        context["num"] = 4
        return context

class Tcount2021View(DetailView):
    template_name = tempurl
    model = Team
    context_object_name = 'teams'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('teamstats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "カウント別"
        context["num"] = 5
        return context

class Tcourse2021View(DetailView):
    template_name = tempurl
    model = Team
    context_object_name = 'teams'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('teamstats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "コース別"
        context["num"] = 6
        return context

class Tbn2021View(DetailView):
    template_name = tempurl
    model = Team
    context_object_name = 'teams'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('teamstats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "打順別"
        context["num"] = 11
        return context

class Tp2021View(DetailView):
    template_name = tempurl
    model = Team
    context_object_name = 'teams'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('teamstats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "点差別"
        context["num"] = 10
        return context

class Tw2021View(DetailView):
    template_name = tempurl
    model = Team
    context_object_name = 'teams'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('teamstats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "曜日別"
        context["num"] = 9
        return context

class Tbase2021View(DetailView):
    template_name = tempurl
    model = Team
    context_object_name = 'teams'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('teamstats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "塁別"
        context["num"] = 7
        return context

class Tm2021View(DetailView):
    template_name = tempurl
    model = Team
    context_object_name = 'teams'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('teamstats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "月別"
        context["num"] = 8
        return context


class Tposi2021View(DetailView):
    template_name = tempurl
    model = Team
    context_object_name = 'teams'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('teamstats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "守備位置別"
        context["num"] = 13
        return context