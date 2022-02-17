from django.urls import path, include
from .views import Team2021View, TeamIntro2021View, TeamPlayerBatt2021View, TeamPlayerPit2021View



urlpatterns = [
    path('', Team2021View.as_view(), name='t2021'),
    path('<int:pk>/', TeamIntro2021View.as_view(), name='ti2021'),
    path('<int:pk>/batt/', include('teamdetail2021.urls')),
    path('<int:pk>/pit/', include('teamdetail2021p.urls')),
    path('<int:pk>/player/batt/', TeamPlayerBatt2021View.as_view(), name='tpb2021'),
    path('<int:pk>/player/pit/', TeamPlayerPit2021View.as_view(), name='tpp2021'),

]