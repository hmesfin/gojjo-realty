from django import template
import re

register = template.Library()

@register.filter(name='format_phone')
def format_phone(value):
    # Assuming value is in the format +19999999999
    phone_number = re.sub(r'\D', '', str(value))  # Remove non-digits

    # Check if the phone number has the correct 11 digits (1 for country code + 10 digits)
    if len(phone_number) == 11 and phone_number.startswith('1'):
        return f"+1({phone_number[1:4]}) {phone_number[4:7]}-{phone_number[7:]}"
    else:
        return value  # Return the original value if it's not valid
