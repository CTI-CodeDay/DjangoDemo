from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>") #string of HTML code

def home_view2(*args, **kwargs):
    return HttpResponse("<h1>Goon Squad!</h1>") #another string of HTML code