from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Think of views as a place that handles your various web pages

def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World!</h1>")