from django.http import HttpResponse
from django.shortcuts import render

def homepage_view(*args, **kwargs):
    return "<h1>Hello World</h1>"
