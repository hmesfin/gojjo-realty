from django.utils.translation import gettext_lazy as _

CONTACT_TYPE_CHOICES = (
    ('client', _('Client')),
    ('vendor', _('Vendor')),
    ('other', _('Other')),
)

ADDRESS_TYPE_CHOICES = (
    ('home', _('Home')),
    ('office', _('Office')),
    ('other', _('Other')),
)

PHONE_TYPE_CHOICES = (
    ('home', _('Home')),
    ('office', _('Office')),
    ('mobile', _('Mobile')),
    ('other', _('Other')),
)

CONTACT_RELATIONSHIP_CHOICES = (
    ('spouse', _('Spouse')),
    ('parent', _('Parent')),
    ('child', _('Child')),
    ('sibling', _('Sibling')),
    ('other', _('Other')),
)

CONTACT_GENDER_CHOICES = (
    ('male', _('Male')),
    ('female', _('Female')),
    ('non_binary', _('Non-Binary')),
    ('refuse_id', _('Refuse to Identify')),
    ('other', _('Other')),
)

CONTACT_PRONOUN_CHOICES = (
    ('he', _('He/Him')),
    ('she', _('She/Her')),
    ('they', _('They/Them')),
    ('other', _('Other')),
)

CONTACT_MARITAL_STATUS_CHOICES = (
    ('single', _('Single')),
    ('married', _('Married')),
    ('divorced', _('Divorced')),
    ('widowed', _('Widowed')),
    ('cohabit', _('Co-Habitating')),
    ('other', _('Other')),
)

CONTACT_EMPLOYMENT_STATUS_CHOICES = (
    ('employed', _('Employed')),
    ('self_employed', _('Self-Employed')),
    ('unemployed', _('Unemployed')),
    ('retired', _('Retired')),
    ('student', _('Student')),
    ('other', _('Other')),
)

CONTACT_EDUCATION_LEVEL_CHOICES = (
    ('high_school', _('High School')),
    ('college', _('College')),
    ('university', _('University')),
    ('graduate', _('Graduate')),
    ('other', _('Other')),
)

CONTACT_INCOME_LEVEL_CHOICES = (
    ('low', _('Low')),
    ('middle', _('Middle')),
    ('high', _('High')),
    ('other', _('Other')),
)

CONTACT_HOUSEHOLD_INCOME_LEVEL_CHOICES = (
    ('less_30', _('Less than $30,000')),
    ('30_60', _('Between $30,000 and $60,000')),
    ('60_100', _('Between $60,000 and $100,000')),
    ('100_150', _('Between $100,000 and $150,000')),
    ('150_200', _('Between $150,000 and $200,000')),
    ('more_200', _('More than $200,000')),
)

CONTACT_PREFERRED_CONTACT_METHOD_CHOICES = (
    ('email', _('Email')),
    ('phone', _('Phone')),
    ('text', _('Text')),
    ('snail_mail', _('Snail Mail')),
    ('other', _('Other')),
)