from django.test import TestCase
from .models import Myphoto,Category

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Hiking= Category(name='Hiking 1')


    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Hiking,Category))

    # Testing Save Method        
 