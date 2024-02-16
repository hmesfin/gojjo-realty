from django import forms

from .models import Contact

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.bootstrap import FormActions
from django_recaptcha.fields import ReCaptchaField

from .models import Contact
from .models import LandingPage

class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'message', 'attending', 'captcha']
        widgets = {
            'attending': forms.Select(attrs={'class': 'form-check-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'captcha': ReCaptchaField()
        }
        labels = {
            'attending': 'Are you attending?'
        }
        help_texts = {
            'attending': 'Please let us know if you are attending.'
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'contact-form'
        self.helper.layout = Layout(
            Row(
                Column(
                    FloatingField('attending', css_class='form-group'),
                ),
            ),
            Row(
                Column(
                    FloatingField('first_name', css_class='form-group'),
                ),
                Column(
                    FloatingField('last_name', css_class='form-group'),
                ),
            ),
            Row(
                Column(
                    FloatingField('email', css_class='form-group'),
                ),
                Column(
                    FloatingField('phone', css_class='form-group'),
                ),
            ),
            FloatingField('message', css_class='form-group'),
            'captcha',
            FormActions(
                Submit('submit', 'Submit', css_class='btn btn-primary')
            )
        )

        self.helper.form_show_labels = False
        self.helper.form_show_errors = True
        self.helper.form_tag = False
        self.helper.render_required_fields = True
        self.helper.error_text_inline = True
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        if not email and not phone:
            raise forms.ValidationError('You must enter either an email address or a phone number.')
        return cleaned_data
    
    def save(self, commit=True):
        instance = super(ContactForm, self).save(commit=False)
        instance.landing_page = LandingPage.objects.get(slug=self.initial['event'])
        if commit:
            instance.save()
        return instance