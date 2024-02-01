from django.urls import path
from .views.views import (
    AgentListView,
    AgentDetailView,
    AgentUpdateView,
)

app_name = 'agents'

urlpatterns = [
    path('', AgentListView.as_view(), name='agent_list'),
    path('agent/<slug:slug>/', AgentDetailView.as_view(), name='agent_detail'),
    path('<int:pk>/update/', AgentUpdateView.as_view(), name='agent_update'),
]