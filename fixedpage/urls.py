from django.urls import path
from .views import TopView, FirstView, ContactView, ContactsendView, NeologismView, SiteView, SearchView, PrivacypolicyView

urlpatterns = [
    path('', TopView.as_view(), name='top'),
    path('first/', FirstView.as_view(), name='first'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact-send/', ContactsendView.as_view(), name='contact-send'),
    path('neologism/', NeologismView.as_view(), name='neologism'),
    path('site/', SiteView.as_view(), name='site'),
    path('search/', SearchView.as_view(), name='search'),
    path('privacypolicy/', PrivacypolicyView.as_view(), name='privacypolicy'),
]