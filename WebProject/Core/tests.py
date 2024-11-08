from django.test import TestCase
from .models import ContactForm

# Create your tests here.
class SingletonModelTestCase(TestCase):
    def test_singleton_creation_and_save(self):
        singleton_instance_0 = ContactForm.load()
        singleton_instance_1 = ContactForm.load()
        singleton_instance_2 = ContactForm.load()
        singleton_instance_3 = ContactForm.load()
        self.assertEqual(ContactForm.objects.all().count(), 1)