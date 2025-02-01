from django.test import TestCase
from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        FAQ.objects.create(question_en="What is Django?", answer_en="A web framework")

    def test_faq_creation(self):
        faq = FAQ.objects.get(question_en="What is Django?")
        self.assertEqual(faq.answer_en, "A web framework")

# Create your tests here.
