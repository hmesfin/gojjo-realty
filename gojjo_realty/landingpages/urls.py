from django.urls import path

from gojjo_realty.landingpages.views.views import LandingPageListView, LandingPageDetailView

app_name = 'events'

urlpatterns = [
    path('', LandingPageListView.as_view(), name='events_list'),
    path('<slug:slug>/', LandingPageDetailView.as_view(), name='event_detail'),
]