from django import forms
from django_recaptcha.fields import ReCaptchaField
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.bootstrap import FormActions
from ..models import ContactMessage
from django.utils.translation import gettext_lazy as _

from gojjo_realty.pages.choices import SUBJECT_CHOICES


class ContactMessageForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'phone', 'subject', 'message', 'captcha']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'contact_message_form'
        self.helper.form_method = 'post'
        self.helper.form_class = 'contact-form'
        self.helper.form_show_labels = False
        self.helper.form_action = reverse_lazy('pages:contact')

        self.helper.layout = Layout(
            FloatingField('first_name', placeholder=_('First Name')),
            FloatingField('last_name', placeholder=_('Last Name')),
            FloatingField('email', placeholder=_('Email')),
            FloatingField('phone', placeholder=_('Phone')),
            FloatingField('subject', placeholder=_('Subject')),
            FloatingField('message', placeholder=_('Message')),
            'captcha',
            FormActions(
                Submit('submit', _('Send message'), css_class='btn btn-primary')
            )
        )