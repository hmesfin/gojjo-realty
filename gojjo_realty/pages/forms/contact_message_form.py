from django import forms
from django_recaptcha.fields import ReCaptchaField
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.bootstrap import FormActions
from ..models import ContactMessage
from django.utils.translation import gettext_lazy as _

from gojjo_realty.utils.choices import SUBJECT_CHOICES

from gojjo_realty.leads.models import Lead
from gojjo_realty.agents.models import Agent


class ContactMessageForm(forms.ModelForm):
    # captcha = ReCaptchaField()

    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'phone', 'subject', 'message', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'contact_message_form'
        self.helper.form_method = 'post'
        self.helper.form_class = 'contact-form'
        self.helper.form_show_labels = False
        self.helper.form_action = reverse_lazy('pages:contact')

        self.helper.layout = Layout(
            Row(
                Column(
                    FloatingField('first_name', css_class='form-group'),
                ),
                Column(
                    FloatingField('last_name', css_class='form-group'),
                )
            ),
            Row(
                Column(
                    FloatingField('email', css_class='form-group'),
                ),
                Column(
                    FloatingField('phone', css_class='form-group'),
                )
            ),
            FloatingField('subject', css_class='form-group'),
            FloatingField('message', css_class='form-group'),
            # 'captcha',
            FormActions(
                Submit('submit', 'Submit', css_class='btn btn-primary')
            )
        )
    
    def send_email(self, send_to_email):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
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
        return True
    
    def save(self):
        instance = super().save(commit=False)
        instance.save()
        return instance
    # def save_lead(self, commit=True):
    #     agent = Agent.objects.filter(slug="aida-tezera").first()
    #     first_name = self.cleaned_data['first_name']
    #     last_name = self.cleaned_data['last_name']
    #     email = self.cleaned_data['email']
    #     phone_number = self.cleaned_data['phone']

    #     # Check if lead with the same email or phone number already exists
    #     if Lead.objects.filter(email=email).exists() or Lead.objects.filter(phone_number=phone_number).exists():
    #         return None
        
    #     lead = Lead.objects.create(
    #         agent=agent,
    #         first_name=first_name,
    #         last_name=last_name,
    #         email=email,
    #         phone_number=phone_number,
    #     )
    #     return lead