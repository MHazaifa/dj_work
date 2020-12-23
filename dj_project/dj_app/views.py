from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (me):
    return HttpResponse ("<h> index page<h1>")
def newpage (firstpage):
    return HttpResponse ("<h1> new page<h1>")