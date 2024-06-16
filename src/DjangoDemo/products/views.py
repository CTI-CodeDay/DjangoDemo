from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1> Welcome to My App! If you have an admin account, type /admin at the end of the URL </h1>")