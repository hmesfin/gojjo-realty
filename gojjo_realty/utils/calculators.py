def calculate_mortgage_payment(financing_data):
    principal = financing_data['loan_amount']
    interest_rate = financing_data['interest_rate'] / 100 / 12
    loan_term = financing_data['loan_term'] * 12
    mortgage_payment = principal * interest_rate * (1 + interest_rate) ** loan_term / ((1 + interest_rate) ** loan_term - 1)
    return mortgage_payment

def calculate_cash_flow(property_data, financing_data):
    total_expenses = property_data['operating_expenses']
    mortgage_payment = calculate_mortgage_payment(financing_data)
    total_expenses += mortgage_payment
    cash_flow = property_data['rental_income'] - total_expenses
    return cash_flow

def calculate_roi(property_data, cash_flow):
    initial_investment = property_data['price'] - property_data['down_payment']
    roi = (cash_flow * 12) / initial_investment * 100
    return roi