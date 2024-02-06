from django.utils.translation import gettext_lazy as _

LINK_CATEGORY_CHOICES = (
    ('affiliates', _('Affiliates')),
    ('footer', _('Footer')),
    ('support', _('Support')),
    ('other', _('Other')),
)

SUBJECT_CHOICES = (
    ('buying', _('Buying')),
    ('selling', _('Selling')),
    ('investing', _('Investing')),
    ('general_question', _('General Question')),
    ('partnership', _('Partnership')),
    ('other', _('Other')),
)

LEGAL_DOCUMENT_CHOICES = (
    ('tos', _('Terms and Conditions')),
    ('privacy', _('Privacy Policy')),
    ('disclaimer', _('Disclaimer')),
    ('other', _('Other')),
)

PAGE_TYPE_CHOICES = (
    ('primary', _('Primary')),
    ('secondary', _('Secondary')),
    ('special', _('Special')),
    ('other', _('Other')),
)

CLIENT_TYPE_CHOICES = (
    ('buyer', _('Buyer')),
    ('seller', _('Seller')),
    ('buyer_seller', _('Buyer/Seller')),
    ('investor', _('investor')),
)