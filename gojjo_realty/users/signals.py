from django.db.models.signals import post_save
from django.dispatch import receiver
from gojjo_realty.users.models import User as GojjoUser
from gojjo_realty.agents.models import Agent

ROLES = {
    'is_agent': 'agent',
    'is_broker': 'broker',
    'is_teamlead': 'teamlead',
    'is_admin': 'admin',
}

@receiver(post_save, sender=GojjoUser)
def create_agent(sender, instance, created, **kwargs):
    if created:
        # Determine the role based on the instance attributes
        role = next((role for attr, role in ROLES.items() if getattr(instance, attr, False)), None)

        if role:
            # Create an Agent object, or get if it already exists
            Agent.objects.get_or_create(user=instance, role=role)

