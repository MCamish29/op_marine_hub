from . import views
from django.urls import path

urlpatterns = [
    path('', views.WantedListing.as_view(), name='home'),
]