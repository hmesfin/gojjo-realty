from django.views.generic import FormView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from gojjo_realty.landingpages.forms import ContactForm

from gojjo_realty.landingpages.models import LandingPage, Venue, Contact

class LandingPageListView(ListView):
    model = LandingPage
    ordering = ['-date']
    template_name = 'events/events_list.html'
    context_object_name = 'events_list'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events_list'] = LandingPage.objects.filter(status='published')
        context['venue'] = Venue.objects.all()
        context['page_title'] = 'Our Upcoming Events'
        context['page_subtitle'] = 'Find the best event for you'
        return context

class LandingPageDetailView(DetailView, FormView):
    model = LandingPage
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
    slug_field ='slug'
    slug_url_kwarg = 'slug'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['attending_form'] = ContactForm()
        context['page_title'] = 'Event'
        context['list_view_url'] = reverse_lazy('events:events_list')
        context['detail_page_title'] = context['event'].title
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.path
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your attendance selection has been recorded successfully.')
            return super().form_valid(form)
        else:
            messages.error(request, 'Sorry, there was an error recording your request. Please try again.')
            return super().form_invalid(form)