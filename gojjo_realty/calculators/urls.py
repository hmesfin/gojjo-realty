from django.urls import path
from gojjo_realty.calculators.views.views import investment_calculator

app_name = 'calculators'

urlpatterns = [
    path('investment-calculator/', investment_calculator, name='investment_calculator'),
]