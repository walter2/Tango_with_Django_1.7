from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': 'Here some bold font.'}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    return HttpResponse('''This is Rango\'s About page.
    <br/><a href='/rango/index'>Back to the Index page.</a>''')