
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from core.views import *
from django.contrib.auth.views import TemplateView

class TestUrls(SimpleTestCase):

    def test_list_url_resolved(self):
        url=reverse('index')
        self.assertEquals(resolve(url).func.view_class, IndexView)


    def test_about_url_resolved(self):
        url=reverse('about')
        self.assertEquals(resolve(url).func.view_class, AboutView)
  

    def test_privacy_url_resolved(self):
        url=reverse('privacy')
        self.assertEquals(resolve(url).func.view_class, PrivacyView)


 