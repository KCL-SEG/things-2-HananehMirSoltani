from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from .forms import ThingForm
from .models import Thing

class ThingFormTest(TestCase):

    def test_thing_form_valid_data(self):
        form = ThingForm(data={
            'name': 'Test Thing',
            'description': 'A test thing description.',
            'quantity': 10
        })
        self.assertTrue(form.is_valid())

    def test_thing_form_invalid_data(self):
        form = ThingForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)  # Assuming all fields are required

class HomeViewTest(TestCase):

    def test_home_view_get(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form')

    def test_home_view_post(self):
        data = {
            'name': 'New Thing',
            'description': 'Description of new thing',
            'quantity': 5
        }
        response = self.client.post(reverse('home'), data)
        self.assertEqual(response.status_code, 302)  # Redirect status
        self.assertEqual(Thing.objects.count(), 1)
        self.assertEqual(Thing.objects.first().name, 'New Thing')
