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