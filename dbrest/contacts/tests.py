#from django.utils import unittest
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from profile import ProfileView

# Create your tests here.

class ContactAPITestCase(TestCase):
    """
    Create a user and use this user for testing
    The test system will user a standalone DB instead of the default DB
    """
    def setUp(self):
        User.objects.create_user('itest', password='itest', email='itest@itest.com')

    def tearDown(self):
        itest = User.objects.get(username='itest')
        itest.delete()

    def test_register(self):
        """
        Test register user 'hahaha'
          please note that: JSON only accept '"' as validate, "'" is not accepted
          And, the server only accept 'raw-data' in PUT, so, you need to stringfy the JSON in ajax data field
        """
        r = Client().put('/contacts/api/auth', data={"username":"hahaha", "password":"hahaha", "email":"hahaha@hahaha.com"})
        self.assertEqual(r.status_code, 200)

    def test_logout(self):
        """ 
        logout and redirect to '/'
        """
        r = Client().get('/contacts/api/auth')
        self.assertEqual(r.status_code, 302)

    def test_login(self):
        """ 
        login use  test password 
        """
        r = Client().post('/contacts/api/auth', {'username':r'itest', 'password':r'itest'})
        print(r.content)
        self.assertEqual(r.status_code, 200)
        self.assertTrue("Success" in r.content)
