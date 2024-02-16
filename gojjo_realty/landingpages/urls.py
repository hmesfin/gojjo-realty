from django.urls import path

from gojjo_realty.landingpages.views.views import EventListView, EventDetailView

app_name = 'events'

urlpatterns = [
    path('', EventListView.as_view(), name='events_list'),
    path('<slug:slug>/', EventDetailView.as_view(), name='event_detail'),
]