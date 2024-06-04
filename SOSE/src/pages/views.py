from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(requests, *args, **kwargs):
    return render(requests, 'home.html', {})
def about_view(requests, *args, **kwargs):
    return render(requests, 'about.html', {})
def contact_view(requests, *args, **kwargs):
    return render(requests, 'contact.html', {})