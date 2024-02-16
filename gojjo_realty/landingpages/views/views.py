from django.views.generic import FormView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from gojjo_realty.landingpages.forms import ContactForm

from gojjo_realty.landingpages.models import LandingPage, Venue, Contact, EventFAQ
from django.utils import timezone

class EventListView(ListView):
    model = LandingPage
    ordering = ['-date']
    template_name = 'events/events_list.html'
    context_object_name = 'events_list'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events_list'] = LandingPage.objects.filter(status='published', date__gte=timezone.now().date())
        context['venue'] = Venue.objects.all()
        context['page_title'] = 'Our Upcoming Events'
        context['page_subtitle'] = 'Find the best event for you'
        return context

class EventDetailView(DetailView, FormView):
    model = LandingPage
    form_class = ContactForm
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['event'] = LandingPage.objects.get(slug=self.kwargs['slug'])
        # context['venue'] = Venue.objects.all()
        context['attending_form'] = ContactForm(initial={'event': self.kwargs['slug']})
        context['faqs'] = EventFAQ.objects.filter(is_published=True)
        context['contact'] = Contact.objects.all()
        context['list_view_url'] = reverse_lazy('events:events_list')
        context['page_title'] = 'Upcoming Events'
        context['detail_page_title'] = self.object.title
        context['page_subtitle'] = 'Find the best event for you'
        return context
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your message has been sent successfully.')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('landingpages:event_detail', kwargs={'slug': self.kwargs['slug']})
    
    def get_initial(self):
        initial = super().get_initial()
        initial['event'] = self.kwargs['slug']
        return initial