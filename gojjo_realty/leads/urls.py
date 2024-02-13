from django.urls import path
from gojjo_realty.leads.views.views import LeadListView, LeadDetailView

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead_list'),
    path('lead/<slug:slug>/', LeadDetailView.as_view(), name='lead_detail'),
]