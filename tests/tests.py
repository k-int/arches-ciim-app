print("hello")

from django.test import TestCase

class BasicTestCase(TestCase):
    def test_object_creation(self):
            self.assertTrue(True)