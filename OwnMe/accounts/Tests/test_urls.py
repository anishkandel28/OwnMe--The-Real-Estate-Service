
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import *


class TestUrls(SimpleTestCase):

    def test_login_url_resolved(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func, login)

    def test_register_url_resolved(self):
        url=reverse('register')
        self.assertEquals(resolve(url).func, register)


    def test_logout_url_resolved(self):
        url=reverse('logout')
        self.assertEquals(resolve(url).func, logout)

    def test_dashboard_url_resolved(self):
        url=reverse('dashboard')
        self.assertEquals(resolve(url).func,dashboard)

              


    


 