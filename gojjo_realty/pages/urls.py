from django.urls import path
from gojjo_realty.pages.views.views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    ServicesListPageView,
    ServiesDetailPageView,
    FAQListPageView,
    TermsPageView,
    PrivacyPageView
    )

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('services/', ServicesListPageView.as_view(), name='services'),
    path('services/<slug:slug>/', ServiesDetailPageView.as_view(), name='service'),
    path('faqs/', FAQListPageView.as_view(), name='faq'),
    path('terms/', TermsPageView.as_view(), name='terms'),
    path('privacy/', PrivacyPageView.as_view(), name='privacy'),
]