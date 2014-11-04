from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': 'Here some bold font.'}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    content_dict = {'message': 'Rango\'s site is growing continuously by the minute.'}
    return render(request, 'rango/about.html', content_dict)