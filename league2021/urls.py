from django.urls import path, include
from .views import La2021View, Lavr2021View, Lavl2021View, Lac2021View, Las2021View, Lavt2021View, Lai2021View,\
    Lacount2021View, Lacourse2021View, Labn2021View, Lap2021View, Law2021View, Labase2021View, Lam2021View, Laposi2021View


urlpatterns = [
    path('<int:pk>/', La2021View.as_view(), name='La'),
    path('<int:pk>/vsright/', Lavr2021View.as_view(), name='Lvsright'),
    path('<int:pk>/vsleft/', Lavl2021View.as_view(), name='Lvsleft'),
    path('<int:pk>/chance/', Lac2021View.as_view(), name='Lchance'),
    path('<int:pk>/stadium/', Las2021View.as_view(), name='Lstadium'),
    path('<int:pk>/vsteam/', Lavt2021View.as_view(), name='Lvsteam'),
    path('<int:pk>/inning/', Lai2021View.as_view(), name='Linning'),
    path('<int:pk>/count/', Lacount2021View.as_view(), name='Lcount'),
    path('<int:pk>/course/', Lacourse2021View.as_view(), name='Lcourse'),
    path('<int:pk>/batnum/', Labn2021View.as_view(), name='Lbatnum'),
    path('<int:pk>/point/', Lap2021View.as_view(), name='Lpoint'),
    path('<int:pk>/week/', Law2021View.as_view(), name='Lweek'),
    path('<int:pk>/base/', Labase2021View.as_view(), name='Lbase'),
    path('<int:pk>/month/', Lam2021View.as_view(), name='Lmonth'),
    path('<int:pk>/position/', Laposi2021View.as_view(), name='Lposi'),

]