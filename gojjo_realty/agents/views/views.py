from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from gojjo_realty.agents.models import Agent, License, SocialAccount, Address, AgentPage

from gojjo_realty.agents.forms.contact_agent import ContactAgentForm
from gojjo_realty.agents.forms.agent_form import AgentForm

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
        agent_slug = self.kwargs.get('slug')
        context['agent_contact_form'] = ContactAgentForm(initial={'agent': agent_slug})
        context['agent_email_main'] = self.object.user.email
        context['agent_alternate_email'] = self.object.alternate_email
        context['licenses'] = License.objects.filter(licensee=self.object)
        context['social_accounts'] = SocialAccount.objects.filter(agent=self.object)
        context['address'] = Address.objects.filter(agent=self.object).first()
        context['page_title'] = "Our Agents"
        context['list_view_url'] = reverse_lazy('agents:agent_list')
        context['page_subtitle'] = "Realtor Extraordinaire"
        context['detail_page_title'] = self.object.get_full_name()
        return context
    
    def agent_email(request, self):
        if self.agent_alternate_email and self.use_alt_email:
            agent_email = self.agent_alternate_email
        else:
            agent_email = self.agent_main_email
        return agent_email
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        agent_first_name = self.object.first_name
        form = ContactAgentForm(request.POST, agent=self.object.slug)
        if form.is_valid():
            form.send_email(self.object.user.email)
            form.save()
            messages.success(request, f'Your message has been sent successfully! {agent_first_name} will get back to you soon.')
            return redirect('agents:agent_detail', slug=self.object.slug)
        else:
            return self.render_to_response(self.get_context_data(agent_contact_form=form))

class MyLinksView(TemplateView):
    model = Agent
    template_name = 'agents/my_links.html'
    context_object_name = 'agent'
    slug_field ='slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agent_slug = self.kwargs.get('slug')
        context['agent'] = Agent.objects.get(slug=agent_slug)
        context['social_accounts'] = SocialAccount.objects.filter(agent=context['agent'])
        context['page_title'] = "My Links"
        context['page_subtitle'] = "Realtor Extraordinaire"
        context['detail_page_title'] = context['agent'].get_full_name()
        return context


class AgentUpdateView(LoginRequiredMixin, UpdateView):
    model = Agent
    form_class = AgentForm
    template_name = 'agents/agent_update.html'

    # def test_func(self):
    #     agent = self.get_object()
    #     if self.request.user == agent.user:
    #         return True
    #     return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update Agent Profile'
        context['page_subtitle'] = 'Update your agent profile'
        return context
    
    def update_agent(request, slug):
        agent = get_object_or_404(Agent, slug=slug)
        if request.method == 'POST':
            form = AgentForm(request.POST, request.FILES, instance=agent)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile has been updated successfully')
                return redirect('agents:agent_detail', slug=slug)
        else:
            form = AgentForm(instance=agent)
        return render(request, 'agents/agent_update.html', {'form': form, 'agent': agent})


    

class AgentCreateView(LoginRequiredMixin, CreateView):
    model = Agent
    form_class = AgentForm
    template_name = 'agents/agent_create.html'
    success_url = reverse_lazy('agents:agent_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create Agent Profile'
        context['page_subtitle'] = 'Create your agent profile'
        return context
    

