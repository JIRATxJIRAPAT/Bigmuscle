from django.test import TestCase,Client
from django.urls import reverse

# Create your tests here.

class AboutViewTestCase(TestCase):

    def test_index(self):
        """ test aboutpage """
        c = Client()
        response = c.get(reverse('about:index'))
        self.assertEqual(response.status_code,200)