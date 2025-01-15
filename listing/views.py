from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wanted
from .forms import WantedForm

# Create your views here.


class WantedListing(generic.ListView):
    """
    This view will list all wanted records and order by updated date.
    """
    queryset = Wanted.objects.all().order_by('-updated_on')
    template_name = 'listing/index.html'
    paginate_by = 3


class PirateDetailView(generic.DetailView):
    """
    This view will show specific pirate details when selected
    """
    model = Wanted
    template_name = 'listing/pirate_detail.html'
    context_object_name = 'pirate'

    def get_object(self, queryset=None):
        return Wanted.objects.get(slug=self.kwargs['slug'])


@login_required
def create_wanted_listing(request):
    """
    This view shows the creation of a new listing.
    
    - If the request is post, validate and save the form data.
    - Else, provide form to create a new listing.
    """
    if request.method == 'POST':
        form = WantedForm(request.POST, request.FILES)
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
    """
    This view will handle editing an existing wanted listing.

    - Check is the logged-in user is the author.
    - If post, validate and save the form data.
    - Else, display existing data to edit.
    """
    wanted_listing = Wanted.objects.get(slug=slug)

    if wanted_listing.author != request.user:
        messages.error(
            request,
            "You are not authorized to edit this wanted listing.")
        return redirect('home')
    if request.method == 'POST':
        form = WantedForm(request.POST, request.FILES, instance=wanted_listing)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "The wanted listing has been updated successfully.")
            return redirect('home')
    else:
        form = WantedForm(instance=wanted_listing)

    return render(
        request,
        'listing/edit_listing.html',
        {'form': form, 'pirate': wanted_listing})


@login_required
def delete_wanted_listing(request, slug):
    """
     This view will handle deleting an existing wanted listing.

    - Check is the logged-in user is the author.
    - If post, delete listing and return to home page.
    - Else, render confirmation page.

    """

    wanted_listing = get_object_or_404(Wanted, slug=slug)

   
    if wanted_listing.author != request.user:
        messages.error(
            request,
            "You are not authorized to delete this wanted listing.")
        return redirect('home')

    if request.method == 'POST':
        wanted_listing.delete()
        messages.success(
            request,
            "The wanted listing has been deleted successfully.")
        return redirect('home')

    return render(
        request,
        'listing/confirm_delete.html',
        {'pirate': wanted_listing})
