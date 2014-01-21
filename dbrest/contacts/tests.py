#from django.utils import unittest
from django.test import TestCase
from django.test.client import Client
from profile import ProfileView

# Create your tests here.

class ContactAPITestCase(TestCase):
    def test_logout(self):
        """ logout and redirect to '/'"""
        r = Client().get('/contacts/api/auth')
        self.assertEqual(r.status_code, 302)

    def test_login(self):
        """ login use  test password """
        r = Client().post('/contacts/api/auth', {'username':'itest', 'password':'itest'})
        print(r.content)
        self.assertEqual(r.status_code, 200)
        self.assertTrue("Success" in r.content)
