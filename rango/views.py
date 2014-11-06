from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category, Page


def index(request):
    '''index() renders the index page.'''
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'boldmessage': 'Has he greeted other worlds/planets as well?',
                    'categories': category_list}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    '''about() renders the index page.'''
    content_dict = {'message': 'Rango\'s site is growing continuously by the minute.'}
    return render(request, 'rango/about.html', content_dict)