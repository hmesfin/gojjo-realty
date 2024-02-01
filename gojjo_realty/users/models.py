from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, BooleanField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from gojjo_realty.users.managers import UserManager


class User(AbstractUser):
    """
    Default custom user model for Gojjo Realty.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = None  # type: ignore
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    email = EmailField(_("email address"), unique=True)
    username = None  # type: ignore
    is_agent = BooleanField(default=False)
    is_teamlead = BooleanField(default=False)
    is_broker = BooleanField(default=False)
    is_lead = BooleanField(default=False)
    is_client = BooleanField(default=False)
    is_admin = BooleanField(default=False)
    is_manager = BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})
    
    def get_role(self):
        if self.is_agent:
            return 'Agent'
        elif self.is_teamlead:
            return 'Team Lead'
        elif self.is_broker:
            return 'Broker'
        elif self.is_lead:
            return 'Lead'
        elif self.is_client:
            return 'Client'
        elif self.is_admin:
            return 'Admin'
        elif self.is_manager:
            return 'Manager'
        else:
            return 'User'
