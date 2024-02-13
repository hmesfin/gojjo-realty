from django.urls import path
from .views.views import (
    AgentListView,
    AgentDetailView,
    AgentUpdateView,
    MyLinksView
)

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name='agent_list'),
    path('agent/<slug:slug>/', AgentDetailView.as_view(), name='agent_detail'),
    path('<slug:slug>/update/', AgentUpdateView.as_view(), name='agent_update'),
    path('my-links/<slug:slug>/', MyLinksView.as_view(), name='my_links'),
]