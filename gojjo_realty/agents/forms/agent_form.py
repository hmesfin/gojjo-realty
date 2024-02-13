from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from tinymce.widgets import TinyMCE

from gojjo_realty.agents.models import Agent, License, SocialAccount

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_bootstrap5.bootstrap5 import FloatingField



class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields = [
            'first_name',
            'last_name',
            'phone',
            'role',
            'agent_photo',
            'gender',
            'gender_id',
            'bio',
            'agent_short_bio',
            'practice_areas',
            'focus_areas',
            'is_published'
            ]

        def __init__(self, *args, **kwargs):
            super(AgentForm, self).__init__(*args, **kwargs)
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
                    FloatingField('gender', css_class='form-group'),
                ),
                    Column(
                        FloatingField('gender_id', css_class='form-group'),
                )
                ),
                Row(Column(
                    FloatingField('phone', css_class='form-group'),
                ),
                    Column(
                    FloatingField('role', css_class='form-group'),
                ),
                ),
                Row(Column(
                    FloatingField('agent_short_bio', css_class='form-group'),
                )
                ),
                Row(Column(
                    FloatingField('bio', css_class='form-group'),
                )
                ),
                Row(Column(
                    FloatingField('focus_areas', css_class='form-group'),
                ),
                    Column(
                    FloatingField('practice_areas', css_class='form-group'),
                ),
                ),
                Row(Column(
                    FloatingField('agent_photo', css_class='form-group'),
                ),
                    Column(
                    FloatingField('is_published', css_class='form-group'),
                ),
                ),
                FormActions(
                    Submit('submit', 'Submit', css_class='btn btn-primary')
                )
            )


class LicenseForm(ModelForm):
    class Meta:
        model = License
        fields = ['number', 'state', 'type', 'expiration_date']
        widgets = {
            'license_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'License Number'}),
            'state': forms.Select(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Type'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Expiration Date'}),
        }
        def __init__(self, *args, **kwargs):
            super(LicenseForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_class = 'contact-form'
            self.helper.form_show_labels = False
            self.helper.layout = Layout(
                Row(Column(
                    FloatingField('license_number', css_class='form-group'),
                ),
                    Column(
                    FloatingField('state', css_class='form-group'),
                )
                ),
            )

class SocialAccountForm(ModelForm):
    class Meta:
        model = SocialAccount
        fields = ['name', 'url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
        }
