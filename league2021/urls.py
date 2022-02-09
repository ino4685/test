from django.urls import path, include
from .views import league2021View, leagueIntro2021View, leaguePlayerBatt2021View, leaguePlayerPit2021View


urlpatterns = [
    path('', league2021View.as_view(), name='l2021'),
    path('<int:pk>/', leagueIntro2021View.as_view(), name='li2021'),
    path('<int:pk>/batt/', include('leaguedetail2021.urls')),
    # path('<int:pk>/pit/', leaguePit2021View.as_view(), name='lp2021'),
    path('<int:pk>/player/batt/', leaguePlayerBatt2021View.as_view(), name='lpb2021'),
    # path('<int:pk>/player/pit/', leaguePlayerPit2021View.as_view(), name='lpp2021'),

]