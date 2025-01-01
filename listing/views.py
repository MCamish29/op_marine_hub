from django.shortcuts import render
from django.views import generic
from .models import Wanted

# Create your views here.
class WantedListing(generic.ListView):
    queryset = Wanted.objects.all()
    template_name = 'listing/index.html'
    paginate_by = 3