from django.utils import unittest
from django.test.client import Client

class HomeTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_home_page(self):
        """ Test the Home page of this """
        c = Client()
        res = c.get('/')
        print(res.content)
        self.assertEqual(res.status_code, 200)
        self.assertTrue('csrftoken' in res.cookies)

