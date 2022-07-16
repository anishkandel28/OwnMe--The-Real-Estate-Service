from django.test import TestCase
from accounts.models import Realtor, CustomUser, CustomUserManager

class TestAppModels(TestCase):
    def test_model_str(self):
        first_name=CustomUser.objects.create(first_name="Anish Shree")
        last_name=CustomUser.objects.create(last_name="Kandel")
        phone=CustomUser.objects.create(phone=9809551746)   
        self.assertEqual(str(name), "Anish Shree")