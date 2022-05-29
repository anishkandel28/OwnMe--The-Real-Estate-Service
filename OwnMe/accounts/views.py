from django.shortcuts import render, redirect
from django.views.generic import (UpdateView, TemplateView)
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse
from .forms import ProfileUpdateForm
from .models import CustomUser

from django.contrib.auth import get_user_model


User = get_user_model()


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


class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = 'accounts/profile.html'
    success_message = _("Profile updated successfully!")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # request.path replacement
        context['profile'] = True
        # Showcase Section Infos
        context['title'] = _("Manage Account")
        context['subtitle'] = _("Manage your Real-Estate account")
        # SEO
        context['page_title'] = _("Impressum")
        context['page_description'] = _("Real estate manager."
                                        "This is our impressum page.")

        return context
