from django.urls import path
from .views import (user_contact
                   )


urlpatterns = [
   
    path('user-contact', user_contact, name='user-contact'),
]
