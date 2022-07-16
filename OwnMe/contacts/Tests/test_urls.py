
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from contacts.views import *


class TestUrls(SimpleTestCase):

    def test_anonymous_contact_url_resolved(self):
        url=reverse('anonymous-contact')
        self.assertEquals(resolve(url).func, anonymous_contact)

    def test_user_contact_url_resolved(self):
        url=reverse('user-contact')
        self.assertEquals(resolve(url).func, user_contact)

    def test_chat_url_resolved(self):
        url=reverse('chat')
        self.assertEquals(resolve(url).func, chat_message)        

    