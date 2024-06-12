from django.http import HttpResponse
from django.shortcuts import render

# Create your views here. place that handles all webpages
# functions or classes in python

def home_view(*args, **kwargs):
    return HttpResponse("<h1> Hello World </h1>")

