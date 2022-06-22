from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_views (*args, **kwargs):
    return HttpResponse('<h1> Hello World </h1>')