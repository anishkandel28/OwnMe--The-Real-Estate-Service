from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.views.generic import (UpdateView, TemplateView)
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
# from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from .forms import ProfileUpdateForm
from .models import CustomUser
from contacts.models import Contact

from django.contrib.auth import get_user_model


User = get_user_model()


def register(request):
    """Register new user function"""
    context = {
        'title': _("Register"),
        'page_title': _("Register Account"),
        'page_description': _("Real estate manager. "
                              "This is the regitration page."),
    }

    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check email
            if User.objects.filter(email=email).exists():
                messages.error(request, _("That email is being used"))
                return redirect('register')
            else:
                # if everything looks good
                user = User.objects.create_user(
                    password=password, email=email, is_active=True,
                    first_name=first_name, last_name=last_name)
                user.save()
                messages.success(
                    request, _("You are now registered and can log in"))
                return redirect('login')
        else:
            messages.error(request, _("Passwords do not match"))
            return redirect('register')
    else:
        return render(request, 'accounts/auth/register.html', context)


def login(request):
    """Login user function"""
    context = {
        'title': _("Login"),
        'page_title': _("Account Login"),
        'page_description': _("Real estate manager. This is the login page."),
    }
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, _("You are now logged in"))
            return redirect('dashboard')
        else:
            messages.error(request, _("Invalid credentials"))
            return redirect('login')
    else:
        return render(request, 'accounts/auth/login.html', context)


def logout(request):
    """Logout user function"""
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, _("You are now logged out"))
        return redirect('index')


