from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from gojjo_realty.agents.models import Agent, License, SocialAccount, Address, AgentPage

from gojjo_realty.agents.forms import AgentForm

class AgentListView(ListView):
    model = Agent
    context_object_name = 'agents'
    template_name = 'agents/agent_list.html'
    ordering = ['created_date']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agents'] = Agent.objects.filter(is_published=True)
        context['agent_page'] = AgentPage.objects.filter(is_published=True).first()
        context['licenses'] = License.objects.all()
        context['social_accounts'] = SocialAccount.objects.all()
        context['page_title'] = 'Our Agents'
        context['page_subtitle'] = 'Find the best agent for you'
        return context

class AgentDetailView(DetailView):
    model = Agent
    context_object_name = 'agent'
    template_name = 'agents/agent_detail.html'
    slug_field ='slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['licenses'] = License.objects.filter(licensee=self.object)
        context['social_accounts'] = SocialAccount.objects.filter(agent=self.object)
        context['addresses'] = Address.objects.filter(agent=self.object)
        context['page_title'] = "Our Agents"
        context['page_subtitle'] = "Realtor Extraordinaire"
        context['detail_page_title'] = self.object.get_full_name()
        return context


class AgentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Agent
    form_class = AgentForm
    template_name = 'agents/agent_update.html'
    success_url = reverse_lazy('agent-list')

    def test_func(self):
        agent = self.get_object()
        if self.request.user == agent.user:
            return True
        return False
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

