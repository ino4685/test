from django.views.generic import ListView, DetailView
from .models import Player, Stats2021

class Pab2021View(DetailView):
    template_name = "player/playerstats.html"
    model = Player
    context_object_name = 'players'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('stats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context["sit"] = "全球"
        context["num"] = 0

        return context


class Pvr2021View(DetailView):
    template_name = "player/playerstats.html"
    model = Player
    context_object_name = 'players'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('stats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "対右"
        context["num"] = 2
        return context

class Pvl2021View(DetailView):
    template_name = "player/playerstats.html"
    model = Player
    context_object_name = 'players'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('stats')  # team -> playerの逆参照なので、related_nameを使用
        return qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "対左"
        context["num"] = 3
        return context

class Pc2021View(DetailView):
    template_name = "player/playerstats.html"
    model = Player
    context_object_name = 'players'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('stats')  # team -> playerの逆参照なので、related_nameを使用
        return qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "得点圏"
        context["num"] = 1
        return context

class Ps2021View(DetailView):
    template_name = "player/playerstats.html"
    model = Player
    context_object_name = 'players'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('stats')  # team -> playerの逆参照なので、related_nameを使用
        return qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "球場別"
        context["num"] = 13
        return context

class Pvt2021View(DetailView):
    template_name = "player/playerstats.html"
    model = Player
    context_object_name = 'players'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('stats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "対チーム別"
        context["num"] = 12
        return context

class Pi2021View(DetailView):
    template_name = "player/playerstats.html"
    model = Player
    context_object_name = 'players'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('stats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "イニング別"
        context["num"] = 4
        return context

class Pcount2021View(DetailView):
    template_name = "player/playerstats.html"
    model = Player
    context_object_name = 'players'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('stats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "カウント別"
        context["num"] = 5
        return context

class Pcourse2021View(DetailView):
    template_name = "player/playerstats.html"
    model = Player
    context_object_name = 'players'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('stats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "コース別"
        context["num"] = 6
        return context

class Pbn2021View(DetailView):
    template_name = "player/playerstats.html"
    model = Player
    context_object_name = 'players'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('stats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "打順別"
        context["num"] = 11
        return context

class Pp2021View(DetailView):
    template_name = "player/playerstats.html"
    model = Player
    context_object_name = 'players'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('stats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "点差別"
        context["num"] = 10
        return context

class Pw2021View(DetailView):
    template_name = "player/playerstats.html"
    model = Player
    context_object_name = 'players'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('stats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "曜日別"
        context["num"] = 9
        return context

class Pbase2021View(DetailView):
    template_name = "player/playerstats.html"
    model = Player
    context_object_name = 'players'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('stats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "塁別"
        context["num"] = 7
        return context

class Pm2021View(DetailView):
    template_name = "player/playerstats.html"
    model = Player
    context_object_name = 'players'

    def get_queryset(self):
        qs = self.model.objects.prefetch_related('stats')  # team -> playerの逆参照なので、related_nameを使用
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sit"] = "月別"
        context["num"] = 8
        return context
