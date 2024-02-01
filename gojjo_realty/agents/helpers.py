from datetime import date

def prevent_future_date(date_value):
    """
    Prevents the entry of future dates in a date field.
    """
    if date_value > date.today():
        raise ValueError("Future dates are not allowed.")

def prevent_past_date(date_value):
    """
    Prevents the entry of past dates in a date field.
    """
    if date_value < date.today():
        raise ValueError("Past dates are not allowed.")
