from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kargs): # *args, **kwargs
    return HttpResponse("<h1>Hello World</h1>") # string of HTMl code
