from django.test import TestCase
from rest_framework.test import APIClient
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(question="What is Django?", answer="Django is a Python web framework.")
    
    def test_faq_creation(self):
        self.assertEqual(self.faq.question, "What is Django?")

class FAQAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.faq = FAQ.objects.create(question="What is Django?", answer="Django is a Python web framework.")
    
    def test_get_faqs(self):
        response = self.client.get('/api/faqs/')
        self.assertEqual(response.status_code, 200)