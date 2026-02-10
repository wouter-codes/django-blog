from django.test import TestCase
from django.test import TestCase
from .forms import CollaborateRequestForm

# Create your tests here.

class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateRequestForm({
            'name': 'name test',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is valid")

    def test_form_is_invalid_name(self):
        """ Test for name field"""
        form = CollaborateRequestForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form is valid")

    def test_form_is_invalid_email(self):
        """ Test for email field"""
        form = CollaborateRequestForm({
            'name': 'name test',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="Form is valid")

    def test_form_is_invalid_message(self):
        """ Test for message field"""
        form = CollaborateRequestForm({
            'name': 'name test',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="Form is valid")