from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from gojjo_real_estate.agents.models import Agent

class AgentListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('agent-list')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.agent = Agent.objects.create(name='John Doe', start_date='2022-01-01')

    def test_agent_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'agents/agent_list.html')
        self.assertContains(response, 'John Doe')

class AgentDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.agent = Agent.objects.create(name='John Doe', start_date='2022-01-01')
        self.url = reverse('agent-detail', kwargs={'pk': self.agent.pk})

    def test_agent_detail_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'agents/agent_detail.html')
        self.assertContains(response, 'John Doe')

class AgentUpdateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.agent = Agent.objects.create(name='John Doe', start_date='2022-01-01')
        self.url = reverse('agent-update', kwargs={'pk': self.agent.pk})

    def test_agent_update_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'agents/agent_update.html')

    def test_agent_update_view_with_invalid_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=' + self.url)
