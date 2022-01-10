from django.urls import path
from .views import Tab2021View, Tvr2021View, Tvl2021View, Tc2021View, Ts2021View, Tvt2021View,\
    Ti2021View, Tcount2021View, Tcourse2021View, Tbn2021View, Tp2021View, Tw2021View, Tbase2021View, Tm2021View,\
    Tposi2021View

urlpatterns = [
    path('', Tab2021View.as_view(), name='tab'),
    path('vsright/', Tvr2021View.as_view(), name='tvsright'),
    path('vsleft/', Tvl2021View.as_view(), name='tvsleft'),
    path('chance/', Tc2021View.as_view(), name='tchance'),
    path('stadium/', Ts2021View.as_view(), name='tstadium'),
    path('vsteam/', Tvt2021View.as_view(), name='tvsteam'),
    path('inning/', Ti2021View.as_view(), name='tinning'),
    path('count/', Tcount2021View.as_view(), name='tcount'),
    path('course/', Tcourse2021View.as_view(), name='tcourse'),
    path('batnum/', Tbn2021View.as_view(), name='tbatnum'),
    path('point/', Tp2021View.as_view(), name='tpoint'),
    path('week/', Tw2021View.as_view(), name='tweek'),
    path('base/', Tbase2021View.as_view(), name='tbase'),
    path('month/', Tm2021View.as_view(), name='tmonth'),
    path('position/', Tposi2021View.as_view(), name='tposi'),

]