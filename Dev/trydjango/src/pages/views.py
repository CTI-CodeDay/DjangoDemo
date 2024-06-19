from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<style>body {text-align:center; background-color:#CAF4FF; font-family:cursive;}</style> <h1>Hello World!</h1> <h2>Really cool seeing you here!</h2> <a href=https://legendary-waffle-pjj7j7x66xqqfrv9-8000.app.github.dev/admin/>Admin Login Page</a>")