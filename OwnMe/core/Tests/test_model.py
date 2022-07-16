from django.test import TestCase
from core.models import Address,Country, State

class TestAppModels(TestCase):
    def test_core_country_model_str(self):
        name=Country.objects.create(name="Nepal")
        shortcut=Country.objects.create(shortcut="npl")
        self.assertEqual(str(name), "Nepal")

    # def test_core_state_model_str(self):
    #     country=State.objects.create(country="Germany")
    #     name=State.objects.create(name="Berlin")
    #     shortcut=State.objects.create(shortcut="Ger")
    #     self.assertEqual(str(name), "Berlin")
