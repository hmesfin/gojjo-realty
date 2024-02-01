from django import forms
from django.forms import ModelForm

from gojjo_realty.agents.models import Agent, License, SocialAccount



class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields = ['user', 'first_name', 'last_name', 'phone', 'agent_photo', 'agent_bio', 'focus_areas', 'gender', 'gender_id']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'agent_photo': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Agent Photo'}),
            'agent_bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Agent Bio'}),
            'focus_areas': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Focus Areas'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'gender_id': forms.Select(attrs={'class': 'form-control'}),
            
        }

class LicenseForm(ModelForm):
    class Meta:
        model = License
        fields = ['number', 'state', 'expiration_date']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'License Number'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Expiration Date'}),
        }

class SocialAccountForm(ModelForm):
    class Meta:
        model = SocialAccount
        fields = ['name', 'url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
        }