from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('''Good day says Rango
    </br> <a href='/rango/about'>About</a>''')

def about(request):
    return HttpResponse('''This is Rango\'s About page.
    <br/><a href='/rango/index'>Back to the Index page.</a>''')