from . import views
from django.urls import path

urlpatterns = [
    path('', views.WantedListing.as_view(), name='home'),
    path('pirate/<slug:slug>/', views.PirateDetailView.as_view(), name='pirate_detail'),
]
