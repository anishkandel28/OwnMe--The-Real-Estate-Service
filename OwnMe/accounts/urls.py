from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (login, register, logout, dashboard, password_reset_request,
                    ProfileUpdateView, AddressView)

urlpatterns = [
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
    
]
