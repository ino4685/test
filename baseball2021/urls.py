from django.urls import path, include
from .views import Home2021View

urlpatterns = [
    path('', Home2021View.as_view(), name='2021'),
    path('team/', include('team2021.urls')),
    path('player/', include('player2021.urls')),
    path('league/', include('league2021.urls')),

]