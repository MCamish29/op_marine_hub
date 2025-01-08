from . import views
from django.urls import path

urlpatterns = [
    path('', views.WantedListing.as_view(), name='home'),
    path('pirate/<slug:slug>/', views.PirateDetailView.as_view(), name='pirate_detail'),
    path('create/', views.create_wanted_listing, name='create_listing'),  
    path('pirate/<slug:slug>/edit/', views.edit_wanted_listing, name='edit_pirate'), 
    path('pirate/<slug:slug>/delete/', views.delete_wanted_listing, name='delete_pirate'),
]
