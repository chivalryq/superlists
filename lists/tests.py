from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from lists.views import home_page

# Create your tests here.
from django.urls import resolve


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response=self.client.get('/')

        html=response.content.decode('utf8')
        expected_html=render_to_string('home.html')
        self.assertEqual(html,expected_html)

        self.assertTemplateUsed(response,'home.html')