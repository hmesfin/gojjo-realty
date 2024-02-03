from django.views.generic import TemplateView, ListView, DetailView
from gojjo_realty.pages.models import (
    HomePage,
    Service,
    CallToAction,
    Testimonial,
    AboutPage,
    ContactPage,
    Service,
    FAQ,
    FAQCategory,
    Legal,
    ServicesPage
    )
from gojjo_realty.agents.models import Agent, AgentPage
from gojjo_realty.pages.models import Service, CallToAction, FAQ, FAQCategory, Legal
from gojjo_realty.blogs.models import Post, Category


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['home_page'] = HomePage.objects.filter(type="primary").first()
        context['about_page'] = AboutPage.objects.filter(type="primary").first()
        context['agents'] = Agent.objects.filter(is_published=True)
        context['agent_page'] = AgentPage.objects.filter(is_published=True).first()
        context['services'] = Service.objects.filter(is_published=True).order_by('created_date')[:3]
        context['call_to_action'] = CallToAction.objects.filter(type="primary").first()
        context['faqs'] = FAQ.objects.filter(is_published=True, category=1).order_by('created_date')[:5]
        context['agents'] = Agent.objects.filter(is_published=True).order_by('created_date')[:3]
        context['blogs'] = Post.objects.filter(published=True).order_by('-created_date')[:3]
        context['testimonials'] = Testimonial.objects.filter(is_published=True).order_by('-created_date')
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
        # context['posts'] = Post.objects.filter(published=True).order_by('-created_date')[:3]
        context['page_title'] = "About Us"
        return context


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactPageView, self).get_context_data(**kwargs)
        context['contact_page'] = ContactPage.objects.filter(type="primary").first()
        context['call_to_action'] = CallToAction.objects.filter(type="secondary").first()
        context['agents'] = Agent.objects.filter(is_published=True).order_by('created_date')[:3]
        context['testimonials'] = Testimonial.objects.filter(is_published=True).order_by('-created_date')
        context['page_title'] = "Contact Us"
        return context


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
    template_name = 'pages/service_detail.html'
    model = Service
    context_object_name = 'service'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


    def get_context_data(self, **kwargs):
        context = super(ServiesDetailPageView, self).get_context_data(**kwargs)
        context['service'] = Service.objects.filter(slug=self.kwargs['slug'])
        context['call_to_action'] = CallToAction.objects.filter(is_published=True).first()
        context['page_title'] = "Our Services"
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