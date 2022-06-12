
from django.urls import path
from .views import (ListingListView, ListingDetailView, search)
from . import views


urlpatterns = [
    path('', ListingListView.as_view(), name='listings'),
   
]
