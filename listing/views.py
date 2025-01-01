from django.shortcuts import render
from django.views import generic
from .models import Wanted

# Create your views here.
class WantedListing(generic.ListView):
    queryset = Wanted.objects.all()
    template_name = 'listing/index.html'
    paginate_by = 3

class PirateDetailView(generic.DetailView):
    model = Wanted
    template_name = 'listing/pirate_detail.html'
    context_object_name = 'pirate'

    def get_object(self, queryset=None):      
        return Wanted.objects.get(slug=self.kwargs['slug'])