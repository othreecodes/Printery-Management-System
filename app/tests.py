from django.test import TestCase

# Create your tests here.

class BaseTestCase(TestCase):

    def setUp(self):
        pass

    def assert_user_can_register(self):
        
