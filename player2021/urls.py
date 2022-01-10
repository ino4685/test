from django.urls import path, include
from .views import Player2021View, PlayerSl2021View, PlayerPl2021View, PlayerBatt2021View, PlayerPit2021View

urlpatterns = [
    path('', Player2021View.as_view(), name='p2021'),
    path('sl/', PlayerSl2021View.as_view(), name='psl2021'),
    path('pl/', PlayerPl2021View.as_view(), name='ppl2021'),
    path('batt/', PlayerBatt2021View.as_view(), name=''),
    path('pit/', PlayerPit2021View.as_view(), name=''),
    path('<int:pk>/', include('detail2021.urls'))

]