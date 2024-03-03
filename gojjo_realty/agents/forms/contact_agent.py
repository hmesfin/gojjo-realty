from django import forms
from django.core.mail import send_mail
from django.conf import settings
from gojjo_realty.agents.models import Agent
from django.utils.translation import gettext_lazy as _

from gojjo_realty.leads.models import Lead

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_bootstrap5.bootstrap5 import FloatingField
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

class ContactAgentForm(forms.Form):
    agent = forms.SlugField(widget=forms.HiddenInput())
    first_name = forms.CharField(label=_("First Name"), max_length=100, widget=forms.TextInput(attrs={'placeholder': _('First Name')}))
    last_name = forms.CharField(label=_("Last Name"), max_length=100, widget=forms.TextInput(attrs={'placeholder': _('Last Name')}))
    email = forms.EmailField(label=_("Email"), widget=forms.EmailInput(attrs={'placeholder': _('Email')}))
    phone = forms.CharField(label=_("Phone"), max_length=100, widget=forms.TextInput(attrs={'placeholder': _('Phone')}))
    message = forms.CharField(label=_("Message"), widget=forms.Textarea(attrs={'placeholder': _('Message')}))
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    def __init__(self, *args, **kwargs):
        self.agent_slug = kwargs.pop('agent', None)
        super(ContactAgentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'contact-form'
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Row(Column(
                FloatingField('first_name', css_class='form-group'),
            ),
                Column(
                FloatingField('last_name', css_class='form-group'),
            )
            ),
            Row(Column(
                FloatingField('email', css_class='form-group'),
            ),
                Column(
                FloatingField('phone', css_class='form-group'),
            )
            ),
            Row( Column(
                FloatingField('message', css_class='form-group'),
            )
            ),
            'captcha',
            FormActions(
            Submit('btnSubmit', _('Submit'), css_class='btn btn-primary')
            )
        )


    def send_email(self, agent_email, use_alt_email=True):
        agent_email = agent_email
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')
        message = self.cleaned_data.get('message')

        
        send_mail(
            f'Contact Request for {first_name} {last_name}',
            f'You have a new contact request from {first_name} {last_name}. Their email is {email}. Their phone number is {phone}. They said: {message}',
            settings.DEFAULT_FROM_EMAIL,
            [agent_email],
            fail_silently=False,
        )
    def save(self):
        agent_slug = self.cleaned_data.get('agent')
        agent_instance = Agent.objects.get(slug=agent_slug)
        email = self.cleaned_data.get('email')
        phone_number = self.cleaned_data.get('phone')
        
        # Check if lead with the same email or phone number already exists
        if Lead.objects.filter(email=email).exists() or Lead.objects.filter(phone_number=phone_number).exists():
            return None
        
        lead = Lead.objects.create(
            agent=agent_instance,
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            email=email,
            phone_number=phone_number,
        )
        return lead