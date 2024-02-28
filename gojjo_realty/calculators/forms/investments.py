from django import forms
from django.utils.translation import gettext_lazy as _
from gojjo_realty.utils.choices import PROPERTY_TYPE_CHOICES, STATE_CHOICES

from gojjo_realty.calculators.models.re_investment import Property, Financing

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Submit, Row, Column

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['property_name', 'property_type', 'property_address', 'city', 'state', 'zip_code', 'property_description', 'property_image', 'sale_price', 'rental_income', 'operating_expenses']
        labels = {
            'property_name': _('Property Name'),
            'property_type': _('Property Type'),
            'property_address': _('Property Address'),
            'city': _('City'),
            'state': _('State'),
            'zip_code': _('Zip Code'),
            'property_description': _('Property Description'),
            'property_image': _('Property Image'),
            'sale_price': _('Sale Price'),
            'rental_income': _('Rental Income'),
            'operating_expenses': _('Operating Expense'),
        }
        widgets = {
            'property_name': forms.TextInput(attrs={'class': 'form-control'}),
            'property_type': forms.Select(attrs={'class': 'form-control'}),
            'property_address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'property_description': forms.Textarea(attrs={'class': 'form-control'}),
            'property_image': forms.FileInput(attrs={'class': 'form-control'}),
            'sale_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'rental_income': forms.NumberInput(attrs={'class': 'form-control'}),
            'operating_expenses': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PropertyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Row(
                Column('property_name', css_class='form-group'),
                Column('property_type', css_class='form-group'),
                Column('property_address', css_class='form-group'),
                Column('city', css_class='form-group'),
                Column('state', css_class='form-group'),
                Column('zip_code', css_class='form-group'),
                Column('property_description', css_class='form-group'),
                Column('property_image', css_class='form-group'),
                Column('sale_price', css_class='form-group'),
                Column('rental_income', css_class='form-group'),
                Column('operating_expenses', css_class='form-group'),
                css_class='form-row'
            ),
            FormActions(
                Submit('submit', 'Save', css_class='btn btn-primary')
            )
        )
        self.fields['property_type'].choices = PROPERTY_TYPE_CHOICES
        self.fields['state'].choices = STATE_CHOICES
        self.fields['sale_price'].required = True
        self.fields['rental_income'].required = True
        self.fields['operating_expenses'].required = True

class FinancingForm(forms.ModelForm):
    class Meta:
        model = Financing
        fields = ['property', 'purchase_price', 'down_payment', 'interest_rate', 'loan_term', 'loan_amount']
        labels = {
            'property': _('Property'),
            'purchase_price': _('Purchase Price'),
            'down_payment': _('Down Payment'),
            'interest_rate': _('Interest Rate'),
            'loan_term': _('Loan Term'),
            'loan_amount': _('Loan Amount'),
        }
        widgets = {
            'property': forms.Select(attrs={'class': 'form-control'}),
            'purchase_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'down_payment': forms.NumberInput(attrs={'class': 'form-control'}),
            'interest_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'loan_term': forms.NumberInput(attrs={'class': 'form-control'}),
            'loan_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(FinancingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Row(
                Column('property', css_class='form-group'),
                Column('purchase_price', css_class='form-group'),
                Column('down_payment', css_class='form-group'),
                Column('interest_rate', css_class='form-group'),
                Column('loan_term', css_class='form-group'),
                Column('loan_amount', css_class='form-group'),
                css_class='form-row'
            ),
            FormActions(
                Submit('submit', 'Save', css_class='btn btn-primary')
            )
        )
        self.fields['property'].queryset = Property.objects.all()
        self.fields['purchase_price'].required = True
        self.fields['down_payment'].required = True
        self.fields['interest_rate'].required = True
        self.fields['loan_term'].required = True
        self.fields['loan_amount'].required = True
