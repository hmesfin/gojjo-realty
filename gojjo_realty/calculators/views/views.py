from django.shortcuts import render
from gojjo_realty.calculators.forms.investments import PropertyForm, FinancingForm
from gojjo_realty.utils.calculators import (calculate_cash_flow, calculate_roi)

def investment_calculator(request):
    property_form = PropertyForm()
    financing_form = FinancingForm()
    if request.method == 'POST':
        property_form = PropertyForm(request.POST, request.FILES)
        financing_form = FinancingForm(request.POST)
        if property_form.is_valid() and financing_form.is_valid():
            property = property_form.save()
            financing = financing_form.save(commit=False)
            financing.property = property
            financing.loan_amount = financing.purchase_price - (financing.purchase_price * (financing.down_payment / 100))
            financing.save()
            cash_flow = calculate_cash_flow(financing, property)
            roi = calculate_roi(financing, property, cash_flow)
            return render(request, 'calculators/investment_calculator.html', {'property_form': property_form, 'financing_form': financing_form, 'cash_flow': cash_flow, 'roi': roi})
    return render(request, 'calculators/investment_calculator.html', {'property_form': property_form, 'financing_form': financing_form})
