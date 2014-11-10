from django.http import HttpResponse
from django.shortcuts import render
from rango.forms import CategoryForm
from rango.models import Category, Page


def index(request):
    '''index() renders the index page.'''
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'boldmessage': 'Has he greeted other worlds/planets as well?',
                    'categories': category_list}
    try:
        pages = Page.objects.order_by('-views')[:5]
        context_dict['pages'] = pages
        context_dict['page_get_success'] = True
    except Category.DoesNotExist:
        pass
    return render(request, 'rango/index.html', context_dict)


def category(request, category_name_slug):
    '''category() takes a request and category_name_slug as
       input. It tries to get the Category object from the data
       base with the category_name_slug and then the objects
       populates the pages key in the context_dict.
    '''
    context_dict = {}
    try:
        category_ = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category_.name
        pages = Page.objects.filter(category=category_)
        context_dict['pages'] = pages
        context_dict['db_get_success'] = True
        #context_dict['category'] = category_ #is requried if more work is done with category
    except Category.DoesNotExist:
        pass
    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    '''add_category() takes a requst and processes the category form 
       if the html method is POST and the form is valid. 
       (The new category data is saved to the database and the user 
       is redirected to the index.html page.)
       Otherwise the category form is presented.
    '''
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = CategoryForm()

    return render(request, 'rango/add_category.html', {'form': form})


def about(request):
    '''about() renders the index page.'''
    content_dict = {'message': 'Rango\'s site is growing continuously by the minute.'}
    return render(request, 'rango/about.html', content_dict)
