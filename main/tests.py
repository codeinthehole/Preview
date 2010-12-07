from django.test import TestCase
from django.test.client import Client

class ViewsTest(TestCase):
    fixtures = ['test_data.json']
    def setUp(self):
        client = Client()
    def test_project_page_exists(self):
        response = self.client.get('/projects/acme/newsite/')
        self.assertEqual(response.status_code, 200)
    def test_client_page_exists(self):
        response = self.client.get('/projects/acme/')
        self.assertEqual(response.status_code, 200)


