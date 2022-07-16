
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from listings.views import *
from listings.forms import AddListingForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# from django.views.generic import (ListView, DetailView)

class TestUrls(SimpleTestCase):

    def test_listings_url_resolved(self):
        url=reverse('listings')
        self.assertEquals(resolve(url).func.view_class, ListingListView)

    # def test_listingsdetail_url_resolved(self):
    #     url=reverse('listing', args="title-id")
    #     self.assertEquals(resolve(url).func.view_class, ListingDetailView)

    def test_addlistings_url_resolved(self):
        url=reverse('add-listing')
        self.assertEquals(resolve(url).func, add_listing)    
            
        


   

 