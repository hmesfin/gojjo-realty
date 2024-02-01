from django.test import TestCase
from gojjo_real_estate.agents.models import Agent, SocialAccount, License
from gojjo_real_estate.users.models import User

class AgentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@example.com')
        self.agent = Agent.objects.create(user=self.user, first_name='John', last_name='Doe')

    def test_agent_creation(self):
        self.assertEqual(self.agent.user, self.user)
        self.assertEqual(self.agent.first_name, 'John')
        self.assertEqual(self.agent.last_name, 'Doe')

    def test_agent_str(self):
        self.assertEqual(str(self.user.agent), 'John Doe')

class SocialAccountModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@example.com')
        self.agent = Agent.objects.create(user=self.user, first_name='John', last_name='Doe')
        self.social_account = SocialAccount.objects.create(agent=self.agent, name='Facebook', url='https://www.facebook.com')

    def test_social_account_creation(self):
        self.assertEqual(self.social_account.agent, self.agent)
        self.assertEqual(self.social_account.name, 'Facebook')
        self.assertEqual(self.social_account.url, 'https://www.facebook.com')

    def test_social_account_str(self):
        self.assertEqual(str(self.social_account), 'Facebook')

class LicenseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@example.com')
        self.agent = Agent.objects.create(user=self.user, first_name='John', last_name='Doe')
        self.license = License.objects.create(licensee=self.agent, number='12345', state='MN', type='Type A')

    def test_license_creation(self):
        self.assertEqual(self.license.licensee, self.agent)
        self.assertEqual(self.license.number, '12345')
        self.assertEqual(self.license.state, 'MN')
        self.assertEqual(self.license.type, 'Type A')

    def test_license_str(self):
        self.assertEqual(str(self.license), '12345')
