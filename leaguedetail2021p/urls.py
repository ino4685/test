from django.urls import path, include
from .views import Lp2021View, Lavrp2021View, Lavlp2021View, Lacp2021View, Lasp2021View, Lavtp2021View, Laip2021View,\
    Lacountp2021View, Lacoursep2021View, Labnp2021View, Lapp2021View, Lawp2021View, Labasep2021View, Lamp2021View, Laposip2021View


urlpatterns = [
    path('', Lp2021View.as_view(), name='Lp'),
    path('vsright/', Lavrp2021View.as_view(), name='Lvsrightp'),
    path('vsleft/', Lavlp2021View.as_view(), name='Lvsleftp'),
    path('chance/', Lacp2021View.as_view(), name='Lchancep'),
    path('stadium/', Lasp2021View.as_view(), name='Lstadiump'),
    path('vsteam/', Lavtp2021View.as_view(), name='Lvsteamp'),
    path('inning/', Laip2021View.as_view(), name='Linningp'),
    path('count/', Lacountp2021View.as_view(), name='Lcountp'),
    path('course/', Lacoursep2021View.as_view(), name='Lcoursep'),
    path('batnum/', Labnp2021View.as_view(), name='Lbatnump'),
    path('point/', Lapp2021View.as_view(), name='Lpointp'),
    path('week/', Lawp2021View.as_view(), name='Lweekp'),
    path('base/', Labasep2021View.as_view(), name='Lbasep'),
    path('month/', Lamp2021View.as_view(), name='Lmonthp'),
    path('position/', Laposip2021View.as_view(), name='Lposip'),

]