from django.test import TestCase,Client
from django.urls import reverse

# Create your tests here.

class homepageViewTestCase(TestCase):

    def test_index(self):
        """ test homepage """
        c = Client()
        response = c.get(reverse('home:index'))
        self.assertEqual(response.status_code,200)