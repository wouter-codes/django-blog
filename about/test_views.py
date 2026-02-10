from django.test import TestCase
from django.urls import reverse
from .forms import CollaborateRequestForm
from .models import About, CollaborateRequest

# Create your tests here.
class TestAboutViews(TestCase):

    def setUp(self):
        self.about = About(title = "About title", content = "About content")
        self.about.save()

    def test_render_about_page_with_collaborate_request_form(self):
        response = self.client.get(reverse(
            'about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About title", response.content)
        self.assertIn(b"About content", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateRequestForm)

    def test_successful_collaborate_request_submission(self):
        """Test for posting a collaborate request"""
        collab_request_data = {
            'name': 'myUsername',
            'email': 'test@email.com',
            'message': 'This is a test collaborate request.',
        }
        response = self.client.post(reverse(
            'about'), collab_request_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content
        )