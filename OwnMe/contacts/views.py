from django.shortcuts import render, redirect
##

from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
##
from django.views.generic import (TemplateView)
from listings.models import Listing


def user_contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #  Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, _("You have already made an inquiry "
                               "for this listing"))
                return redirect('listing', listing_id)

        contact = Contact(listing_id=listing_id, phone=phone, message=message,
                          user_id=user_id)

        contact.save()


class AdminContactView(TemplateView):
    # TODO finish this crap
    template_name = 'admin/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.get(id=5)
        return context
