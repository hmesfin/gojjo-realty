from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from gojjo_realty.pages.models import (
    HomePage,
    Service,
    CallToAction,
    Testimonial,
    AboutPage,
    ContactPage,
    FAQ,
    FAQCategory,
    Legal,
    ServicesPage,
    )
from gojjo_realty.pages.forms.contact_message_form import ContactMessageForm
from gojjo_realty.agents.models import Agent, AgentPage
from gojjo_realty.pages.models import Service, CallToAction, FAQ, FAQCategory, Legal
from gojjo_realty.blogs.models import Post, Category
from gojjo_realty.leads.models import Lead


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['home_page'] = HomePage.objects.filter(type="primary").first()
        context['about_page'] = AboutPage.objects.filter(type="primary").first()
        # context['agents'] = Agent.objects.filter(is_published=True)
        context['agent_page'] = AgentPage.objects.filter(is_published=True).first()
        context['services'] = Service.objects.filter(is_published=True).order_by('created_date')[:3]
        context['call_to_action'] = CallToAction.objects.filter(type="primary").first()
        context['faqs'] = FAQ.objects.filter(is_published=True, category=1).order_by('created_date')[:5]
        context['agents'] = Agent.objects.filter(is_published=True).order_by('created_date')[:3]
        context['blogs'] = Post.objects.filter(published=True).order_by('-created_date')[:3]
        context['testimonials'] = Testimonial.objects.filter(is_published=True).order_by('-created_date')
        if 'contact_form' not in context:
            context['contact_form'] = ContactMessageForm(self.request.POST or None)
        context['categories'] = Category.objects.all()
        context['page_title'] = "Home"
        return context


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context['about_page'] = AboutPage.objects.filter(type="primary").first()
        context['call_to_action'] = CallToAction.objects.filter(type="secondary").first()
        context['agents'] = Agent.objects.filter(is_published=True).order_by('created_date')[:3]
        context['testimonials'] = Testimonial.objects.filter(is_published=True).order_by('-created_date')
        context['blogs'] = Post.objects.filter(published=True).order_by('-created_date')[:3]
        context['page_title'] = "About Us"
        return context


class ContactPageView(SuccessMessageMixin, TemplateView, FormView):
    template_name = 'pages/contact.html'
    form_class = ContactMessageForm
    success_message = 'Your message has been sent successfully! We will get back to you soon. Thank you!'
    success_url = reverse_lazy('pages:contact')
    

    def get_context_data(self, **kwargs):
        context = super(ContactPageView, self).get_context_data(**kwargs)
        context['contact_page'] = ContactPage.objects.filter(type="primary").first()
        if 'contact_form' not in context:
            context['contact_form'] = ContactMessageForm(self.request.POST or None)
        context['call_to_action'] = CallToAction.objects.filter(type="secondary").first()
        context['page_title'] = "Contact Us"
        return context
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def post(self, request, *args, **kwargs):
        send_to_email = ContactPage.objects.filter(type="primary").first().primary_email
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_subject = f'New Contact Message from {first_name} {last_name}'
            email_message = f'You have a new contact message from {first_name} {last_name}.\n\n'
            email_message += f'Email: {email}\n\n'
            email_message += f'Phone: {phone}\n\n'
            email_message += f'Subject: {subject}\n\n'
            email_message += f'Message: {message}\n\n'
            send_to = [send_to_email,]
            send_mail(
                email_subject,
                email_message,
                email,
                send_to,
                fail_silently=False
            )
            return super().form_valid(form)
        else:
            messages.error(request, 'There was an error sending your message. Please try again.')
            return super().form_invalid(form)



class ServicesListPageView(ListView):
    template_name = 'pages/services.html'
    model = Service
    context_object_name = 'services'
    paginate_by = 3
    ordering = ['created_date']

    def get_context_data(self, **kwargs):
        context = super(ServicesListPageView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.filter(is_published=True).order_by('created_date')
        context['service_page'] = ServicesPage.objects.filter(type="primary").first()
        context['call_to_action'] = CallToAction.objects.filter(is_published=True).first()
        context['page_title'] = "Our Services"
        return context
    

class ServiesDetailPageView(DetailView):
    model = Service
    template_name = 'pages/service_detail.html'
    context_object_name = 'service'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


    def get_context_data(self, **kwargs):
        context = super(ServiesDetailPageView, self).get_context_data(**kwargs)
        context['service_page'] = ServicesPage.objects.filter(type="primary").first()
        context['call_to_action'] = CallToAction.objects.filter(is_published=True).first()
        context['page_title'] = "Our Services"
        context['list_view_url'] = reverse_lazy('pages:services')
        context['detail_page_title'] = self.object.name
        return context


class FAQListPageView(TemplateView):
    template_name = 'pages/faqs.html'

    def get_context_data(self, **kwargs):
        context = super(FAQListPageView, self).get_context_data(**kwargs)
        context['faqs'] = FAQ.objects.filter(is_published=True).order_by('created_date')
        context['category'] = FAQCategory.objects.all()
        context['page_title'] = "FAQs"
        return context


class TermsPageView(TemplateView):
    template_name = 'pages/terms.html'

    def get_context_data(self, **kwargs):
        context = super(TermsPageView, self).get_context_data(**kwargs)
        context['terms'] = Legal.objects.filter(document_type="tos").first()
        context['page_title'] =  "Terms of Use"
        return context
    
class PrivacyPageView(TemplateView):
    template_name = 'pages/privacy.html'

    def get_context_data(self, **kwargs):
        context = super(PrivacyPageView, self).get_context_data(**kwargs)
        context['privacy'] = Legal.objects.filter(document_type="privacy").first()
        context['page_title'] =  "Privacy Policy"
        return context