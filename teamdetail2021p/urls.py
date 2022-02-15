from django.urls import path
from .views import Tap2021View, Tvrp2021View, Tvlp2021View, Tcp2021View, Tsp2021View, Tvtp2021View,\
    Tip2021View, Tcountp2021View, Tcoursep2021View, Tbnp2021View, Tpp2021View, Twp2021View, Tbasep2021View, Tmp2021View,\
    Tposip2021View

urlpatterns = [
    path('', Tap2021View.as_view(), name='tap'),
    path('vsright/', Tvrp2021View.as_view(), name='tvsrightp'),
    path('vsleft/', Tvlp2021View.as_view(), name='tvsleftp'),
    path('chance/', Tcp2021View.as_view(), name='tchancep'),
    path('stadium/', Tsp2021View.as_view(), name='tstadiump'),
    path('vsteam/', Tvtp2021View.as_view(), name='tvsteamp'),
    path('inning/', Tip2021View.as_view(), name='tinningp'),
    path('count/', Tcountp2021View.as_view(), name='tcountp'),
    path('course/', Tcoursep2021View.as_view(), name='tcoursep'),
    path('batnum/', Tbnp2021View.as_view(), name='tbatnump'),
    path('point/', Tpp2021View.as_view(), name='tpointp'),
    path('week/', Twp2021View.as_view(), name='tweekp'),
    path('base/', Tbasep2021View.as_view(), name='tbasep'),
    path('month/', Tmp2021View.as_view(), name='tmonthp'),
    path('position/', Tposip2021View.as_view(), name='tposip'),

]