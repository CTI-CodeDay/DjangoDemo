from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.

def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")