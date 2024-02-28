from django.utils.translation import gettext_lazy as _

ROLE_CHOICES = (
    ('agent', _('Agent')),
    ('broker', _('Broker')),
    ('teamlead', _('Team Lead')),
    ('employee', _('Employee')),
)

ADDRESS_TYPE_CHOICES = (
    ('home', _('Home')),
    ('office', _('Office')),
    ('mailing', _('Mailing')),
    ('other', _('Other')),
)
SOCIAL_ACCOUNT_CHOICES = (
    ('facebook', _('Facebook')),
    ('twitter', _('Twitter')),
    ('instagram', _('Instagram')),
    ('linkedin', _('LinkedIn')),
    ('pinterest', _('Pinterest')),
    ('youtube', _('YouTube')),
    ('tiktok', _('TikTok')),
)

LICENSE_TYPE_CHOICES = (
    ('salesperson', _('Salesperson')),
    ('broker', _('Broker')),
    ('assciate_broker', _('Associate Broker')),
)

GENDER_CHOICES = (
    ('male', _('Male')),
    ('female', _('Female')),
    ('refuse_id', _('Refuse to Identify')),
)

GENDER_ID_CHOICES = (
    ('he_him', _('He/Him')),
    ('she_her', _('She/Her')),
    ('they_them', _('They/Them')),
    ('refuse_id', _('Refuse to Identify')),
)

STATE_CHOICES = (
    ('AL', _('Alabama')),
    ('AK', _('Alaska')),
    ('AZ', _('Arizona')),
    ('AR', _('Arkansas')),
    ('CA', _('California')),
    ('CO', _('Colorado')),
    ('CT', _('Connecticut')),
    ('DE', _('Delaware')),
    ('DC', _('District Of Columbia')),
    ('FL', _('Florida')),
    ('GA', _('Georgia')),
    ('HI', _('Hawaii')),
    ('ID', _('Idaho')),
    ('IL', _('Illinois')),
    ('IN', _('Indiana')),
    ('IA', _('Iowa')),
    ('KS', _('Kansas')),
    ('KY', _('Kentucky')),
    ('LA', _('Louisiana')),
    ('ME', _('Maine')),
    ('MD', _('Maryland')),
    ('MA', _('Massachusetts')),
    ('MI', _('Michigan')),
    ('MN', _('Minnesota')),
    ('MS', _('Mississippi')),
    ('MO', _('Missouri')),
    ('MT', _('Montana')),
    ('NE', _('Nebraska')),
    ('NV', _('Nevada')),
    ('NH', _('New Hampshire')),
    ('NJ', _('New Jersey')),
    ('NM', _('New Mexico')),
    ('NY', _('New York')),
    ('NC', _('North Carolina')),
    ('ND', _('North Dakota')),
    ('OH', _('Ohio')),
    ('OK', _('Oklahoma')),
    ('OR', _('Oregon')),
    ('PA', _('Pennsylvania')),
    ('RI', _('Rhode Island')),
    ('SC', _('South Carolina')),
    ('SD', _('South Dakota')),
    ('TN', _('Tennessee')),
    ('TX', _('Texas')),
    ('UT', _('Utah')),
    ('VT', _('Vermont')),
    ('VA', _('Virginia')),
    ('WA', _('Washington')),
    ('WV', _('West Virginia')),
    ('WI', _('Wisconsin')),
    ('WY', _('Wyoming')),
    ('AS', _('American Samoa')),
    ('GU', _('Guam')),
    ('MP', _('Northern Mariana Islands')),
    ('PR', _('Puerto Rico')),
    ('UM', _('United States Minor Outlying Islands')),
    ('VI', _('Virgin Islands')),
    ('AA', _('Armed Forces Americas')),
    ('AP', _('Armed Forces Pacific')),
    ('AE', _('Armed Forces Others')),
)

CONTACT_TYPE_CHOICES = (
    ('lead', _('Lead')),
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

LINK_CATEGORY_CHOICES = (
    ('affiliates', _('Affiliates')),
    ('lenders', _('Lenders')),
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

USER_EMAIL_TYPE_CHOICES = (
    ('subscriber_welcome', _('Welcome Subscriber')),
    ('new_user_welcome', _('New User Welcome')),
    ('email_verification', _('Email Verification')),
    ('subscriber_verification', _('Subscriber Verification')),
    ('password_reset', _('Password Reset')),
    ('other', _('Other')),
)

USER_EMAIL_STATUS_CHOICES = (
    ('pending', _('Pending')),
    ('sent', _('Sent')),
    ('failed', _('Failed')),
    ('other', _('Other')),
)

USER_EMAIL_TEMPLATE_CHOICES = (
    ('html', _('HTML')),
    ('text', _('Text')),
    ('other', _('Other')),
)

EVENT_TYPE_CHOICES = (
    ('open_house', _('Open House')),
    ('workshop', _('Workshop')),
    ('trade_show', _('Trade Show')),
    ('showing', _('Showing')),
    ('meeting', _('Meeting')),
    ('other', _('Other')),
)

EVENT_STATUS_CHOICES = (
    ('draft', _('Draft')),
    ('published', _('Published')),
    ('cancelled', _('Cancelled')),
    ('other', _('Other')),
)

EVENT_ATTENDANCE_CHOICES = (
    ('yes', _('Yes')),
    ('no', _('No')),
    ('maybe', _('Maybe')),
    ('other', _('Other')),
)

PROPERTY_TYPE_CHOICES = (
    ('single_family', _('Single Family')),
    ('condo', _('Condo')),
    ('townhome', _('Townhome')),
    ('multifamily', _('Multifamily')),
    ('apartment', _('Apartment')),
    ('commercial', _('Commercial')),
    ('land', _('Land')),
    ('other', _('Other')),
)

LOAN_TYPE_CHOICES = (
    ('conventional', _('Conventional')),
    ('fha', _('FHA')),
    ('va', _('VA')),
    ('usda', _('USDA')),
    ('other', _('Other')),
)