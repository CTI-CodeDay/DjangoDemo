from django.http import HttpResponse
from django.shortcuts import render

def home_view(*args, **kwargs):
	return HttpResponse("<h1>Hello World</h1>") # string of HTML code
