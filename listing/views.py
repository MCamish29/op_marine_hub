from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wanted
from .forms import WantedForm



# Create your views here.
class WantedListing(generic.ListView):
    queryset = Wanted.objects.all().order_by('-updated_on')
    template_name = 'listing/index.html'
    paginate_by = 3

class PirateDetailView(generic.DetailView):
    model = Wanted
    template_name = 'listing/pirate_detail.html'
    context_object_name = 'pirate'

    def get_object(self, queryset=None):      
        return Wanted.objects.get(slug=self.kwargs['slug'])

@login_required
def create_wanted_listing(request):
    if request.method == 'POST':
        form = WantedForm(request.POST)
        if form.is_valid():            
            wanted_listing = form.save(commit=False)
            wanted_listing.author = request.user  
            wanted_listing.save() 
            messages.add_message(
                request, messages.SUCCESS,
                'Thank you for your submission'
            )
            return redirect('home') 
    else:
        form = WantedForm()
    
    return render(request, 'listing/create_listing.html', {'form': form})

@login_required
def edit_wanted_listing(request, slug):
    wanted_listing = Wanted.objects.get(slug=slug)

    # Check if the logged-in user is the author
    if wanted_listing.author != request.user:
        messages.error(request, "You are not authorized to edit this listing.")
        return redirect('home')  
    if request.method == 'POST':
        form = WantedForm(request.POST, instance=wanted_listing)
        if form.is_valid():
            form.save()
            messages.success(request, "The listing has been updated successfully.")
            return redirect('home') 
    else:
        form = WantedForm(instance=wanted_listing)

    return render(request, 'listing/edit_listing.html', {'form': form, 'pirate': wanted_listing})
