from django.urls import path
from .views import Pab2021View, Pvr2021View, Pvl2021View, Pc2021View, Ps2021View, Pvt2021View,\
    Pi2021View, Pcount2021View, Pcourse2021View, Pbn2021View,Pp2021View, Pw2021View, Pbase2021View, Pm2021View

urlpatterns = [
    path('', Pab2021View.as_view(), name='ab'),
    path('vsright/', Pvr2021View.as_view(), name='vsright'),
    path('vsleft/', Pvl2021View.as_view(), name='vsleft'),
    path('chance/', Pc2021View.as_view(), name='chance'),
    path('stadium/', Ps2021View.as_view(), name='stadium'),
    path('vsteam/', Pvt2021View.as_view(), name='vsteam'),
    path('inning/', Pi2021View.as_view(), name='inning'),
    path('count/', Pcount2021View.as_view(), name='count'),
    path('course/', Pcourse2021View.as_view(), name='course'),
    path('batnum/', Pbn2021View.as_view(), name='batnum'),
    path('point/', Pp2021View.as_view(), name='point'),
    path('week/', Pw2021View.as_view(), name='week'),
    path('base/', Pbase2021View.as_view(), name='base'),
    path('month/', Pm2021View.as_view(), name='month'),

]