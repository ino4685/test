from django.urls import path, include
from .views import La2021View, Lavr2021View, Lavl2021View, Lac2021View, Las2021View, Lavt2021View, Lai2021View,\
    Lacount2021View, Lacourse2021View, Labn2021View, Lap2021View, Law2021View, Labase2021View, Lam2021View, Laposi2021View


urlpatterns = [
    path('', La2021View.as_view(), name='La'),
    path('vsright/', Lavr2021View.as_view(), name='Lvsright'),
    path('vsleft/', Lavl2021View.as_view(), name='Lvsleft'),
    path('chance/', Lac2021View.as_view(), name='Lchance'),
    path('stadium/', Las2021View.as_view(), name='Lstadium'),
    path('vsteam/', Lavt2021View.as_view(), name='Lvsteam'),
    path('inning/', Lai2021View.as_view(), name='Linning'),
    path('count/', Lacount2021View.as_view(), name='Lcount'),
    path('course/', Lacourse2021View.as_view(), name='Lcourse'),
    path('batnum/', Labn2021View.as_view(), name='Lbatnum'),
    path('point/', Lap2021View.as_view(), name='Lpoint'),
    path('week/', Law2021View.as_view(), name='Lweek'),
    path('base/', Labase2021View.as_view(), name='Lbase'),
    path('month/', Lam2021View.as_view(), name='Lmonth'),
    path('position/', Laposi2021View.as_view(), name='Lposi'),

]