from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wanted_listing(request):
    return HttpResponse("One Piece Rules!")