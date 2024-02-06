from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField
from gojjo_realty.contacts.models.contacts import Contact, ContactAddress, Relationship, ContactAdditionalInfo

class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['agent', 'first_name', 'last_name', 'email', 'phone_number', 'phone_type']
        widgets = {
            'phone_number': PhoneNumberField(attrs={'class': 'form-control'}),
            'phone_type': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'agent': forms.Select(attrs={'class': 'form-control'}),

        }
        labels = {
            'agent': _('Agent'),
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'email': _('Email'),
            'phone_number': _('Phone Number'),
            'phone_type': _('Phone Type'),
        }
        error_messages = {
            'phone_number': {
                'invalid': _("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
            },
            'phone_type': {
                'required': _("Phone type is required")
            },
            'email': {
                'required': _("Email is required")
            },
            'first_name': {
                'required': _("First name is required")
            },
            'last_name': {
                'required': _("Last name is required")
            },
            'agent': {
                'required': _("Agent is required")
            }
        }

class UpdateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'agent',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'phone_type',
            'birthdate',
            'gender',
            'pronoun',
            'can_text',
            'contact_type',
            'can_email',
            'can_snail_mail',
            'household_income_level',
            'preferred_contact_method',
            ]
        widgets = {
            'phone_number': PhoneNumberField(attrs={'class': 'form-control'}),
            'phone_type': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'agent': forms.Select(attrs={'class': 'form-control'}),
            'birthdate': forms.DateInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'pronoun': forms.Select(attrs={'class': 'form-control'}),
            'can_text': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'contact_type': forms.Select(attrs={'class': 'form-control'}),
            'can_email': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'can_snail_mail': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'household_income_level': forms.Select(attrs={'class': 'form-control'}),
            'preferred_contact_method': forms.Select(attrs={'class': 'form-control'}),

        }
        labels = {
            'agent': _('Agent'),
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'email': _('Email'),
            'phone_number': _('Phone Number'),
            'phone_type': _('Phone Type'),
            'birthdate': _('Birthdate'),
            'gender': _('Gender'),
            'pronoun': _('Pronoun'),
            'can_text': _('Can Text'),
            'contact_type': _('Contact Type'),
            'can_email': _('Can Email'),
            'can_snail_mail': _('Can Snail Mail'),
            'household_income_level': _('Household Income Level'),
            'preferred_contact_method': _('Preferred Contact Method'),
        }
        error_messages = {
            'phone_number': {
                'invalid': _("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
            },
            'phone_type': {
                'required': _("Phone type is required")
            },
            'email': {
                'required': _("Email is required")
            },
            'first_name': {
                'required': _("First name is required")
            },
            'last_name': {
                'required': _("Last name is required")
            },
            'agent': {
                'required': _("Agent is required")
            },
            'birthdate': {
                'required': _("Birthdate is required")
            },
            'gender': {
               'required': _("Gender is required")
            },
            'pronoun': {
               'required': _("Pronoun is required")
            },
            'can_text': {
               'required': _("Can Text is required")
            },
            'contact_type': {
               'required': _("Contact Type is required")
            },
            'can_email': {
               'required': _("Can Email is required")
            },
            'can_snail_mail': {
               'required': _("Can Snail Mail is required")
            },
            'household_income_level': {
               'required': _("Household Income Level is required")
            },
            'preferred_contact_method': {
               'required': _("Preferred Contact Method is required")
            },
        }