from django.shortcuts import render
from django.http import HttpResponse

# Create your tests here.
def home_view(*args,**kwargs):
    return HttpResponse("<h1>Hello World </h1>")
# Create your views here.
