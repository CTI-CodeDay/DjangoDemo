from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore

def home_view(*args, **kwargs):
    return HttpResponse("h1>Hello World</h1>")
