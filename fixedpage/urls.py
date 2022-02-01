from django.urls import path
from .views import TopView, FirstView, ContactView, NeologismView, PrivacypolicyView

urlpatterns = [
    path('', TopView.as_view(), name='top'),
    path('first/', FirstView.as_view(), name='first'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('neologism/', NeologismView.as_view(), name='neologism'),
    path('privacypolicy/', PrivacypolicyView.as_view(), name='privacypolicy'),
]