from . import views
from django.urls import path

urlpatterns = [
    path('', views.WantedListing.as_view(), name='home'),
    path('pirate/<slug:slug>/', views.PirateDetailView.as_view(), name='pirate_detail'),
    path('create/', views.create_wanted_listing, name='create_listing'),  # New path for creating listings
    path('pirate/<slug:slug>/edit/', views.edit_wanted_listing, name='edit_pirate'), # New path to edit the listings
]
