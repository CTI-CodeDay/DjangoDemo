from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs): #*args, **kwargs
    return HttpResponse('<h1>Hello World</h1>') # string of HTML code

def secondary_view(*args, **kwargs): #*args, **kwargs
    return HttpResponse('<h1>I just made a new view and a new URL route -Colin Nguyen</h1>')