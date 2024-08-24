from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
	return HttpResponse("<h1>Hello world!</h1>")

def todo_view(*args, **kwargs):
	return HttpResponse("<h1>TODO</h1><p>Work in progress</p>")
