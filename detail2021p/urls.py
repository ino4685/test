from django.urls import path
from .views import Pap2021View, Pvrp2021View, Pvlp2021View, Pcp2021View, Psp2021View, Pvtp2021View,\
    Pip2021View, Pcountp2021View, Pcoursep2021View, Pbnp2021View, Ppp2021View, Pwp2021View, Pbasep2021View, Pmp2021View

urlpatterns = [
    path('', Pap2021View.as_view(), name='ap'),
    path('vsright/', Pvrp2021View.as_view(), name='vsrightp'),
    path('vsleft/', Pvlp2021View.as_view(), name='vsleftp'),
    path('chance/', Pcp2021View.as_view(), name='chancep'),
    path('stadium/', Psp2021View.as_view(), name='stadiump'),
    path('vsteam/', Pvtp2021View.as_view(), name='vsteamp'),
    path('inning/', Pip2021View.as_view(), name='inningp'),
    path('count/', Pcountp2021View.as_view(), name='countp'),
    path('course/', Pcoursep2021View.as_view(), name='coursep'),
    path('batnum/', Pbnp2021View.as_view(), name='batnump'),
    path('point/', Ppp2021View.as_view(), name='pointp'),
    path('week/', Pwp2021View.as_view(), name='weekp'),
    path('base/', Pbasep2021View.as_view(), name='basep'),
    path('month/', Pmp2021View.as_view(), name='monthp'),

]