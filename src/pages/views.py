from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def view_home(*args, **kwargs):
    return HttpResponse("<h1>Hey, how's it been?</h1>")