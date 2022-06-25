from django.shortcuts import get_object_or_404, render
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (ListView,DetailView )
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from decimal import Decimal
from django.utils.html import format_html
from .models import Listing
from core.models import State
from django.shortcuts import render, redirect
from django.http import HttpResponse



class ListingListView(ListView):
    model = Listing
    template_name = 'listings/listings.html'
    paginate_by = 4
    object_list = Listing.objects.order_by('-created').filter(
        is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listings'] = self.object_list  # TODO change this bullshit
        # Showcase Section Infos
        context['title'] = _("Browse our properties")
        # SEO
        context['page_title'] = _("Browse Property Listings")
        context['page_description'] = _("Real estate manager."
                                        "Browse all properties we are "
                                        "offering.")
        return context

class ListingDetailView(DetailView):
    model = Listing
    template_name = 'listings/listing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['subtitle'] = format_html(f'<i class="fas fa-map-marker"></i>'
                                          f' {self.object.address}')
        # SEO
        context['page_title'] = self.object.title
        context['page_description'] = _("Real estate manager."
                                        "Description and attribute listing of "
                                        "a specific object you are "
                                        "interested in.")
        return context


