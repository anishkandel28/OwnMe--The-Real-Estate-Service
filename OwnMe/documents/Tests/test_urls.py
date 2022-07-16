
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from documents.views import *
from django.views.generic.detail import DetailView

class TestUrls(SimpleTestCase):

    def test_listings_url_resolved(self):
        url=reverse('user-docs')
        self.assertEquals(resolve(url).func.view_class, UserDocumentView)

  
        


   

 
    