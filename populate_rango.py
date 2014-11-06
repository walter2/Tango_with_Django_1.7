import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django

django.setup()

from rango.models import Category, Page


def populate():
    '''populate() holds the data that is being fed into the database.'''
    python_cat = add_cat(name='Python',
                         views=128,
                         likes=64)

    add_page(cat=python_cat,
             title='Official Python Tutorial',
             url='http://docs.python.org/2/tutorial/')

    add_page(cat=python_cat,
             title='How to think like a Computer Scientist',
             url='http://www.greenteapress.com/thinkpython/')

    add_page(cat=python_cat,
             title='Learn Python in 10 Minutes',
             url='http://www.korokithakis.net/tutorials/python/')

    django_cat = add_cat(name='Django',
                         views=64,
                         likes=32)

    add_page(cat=django_cat,
        title='Test Driven Development with Python',
        url='http://chimera.labs.oreilly.com/books/1234000000754/ch01.html')

    add_page(cat=django_cat,
        title='Django Girls',
        url='http://djangogirls.org/')

    add_page(cat=django_cat,
             title='Official Django Tutorial',
             url='https://docs.djangoproject.com/en/1.5/intro/tutorial01/')

    add_page(cat=django_cat,
             title='Django Rocks',
             url='http://www.djangorocks.com/')

    add_page(cat=django_cat,
             title='How to Tango with Django',
             url='http://www.tangowithdjango.com/')

    frame_cat = add_cat(name='Other Frameworks',
                        views=32,
                        likes=16)

    add_page(cat=frame_cat,
             title='Bottle',
             url='http://bottlepy.org/docs/dev/')

    add_page(cat=frame_cat,
             title='Flask',
             url='http://flask.pocoo.org')

    #Print out what is added to the user.
    for category_ in Category.objects.all():
        for page in Page.objects.filter(category=category_):
            print('- {0} - {1}'.format(str(category_), str(page)))

def add_page(cat, title, url, views=0):
    '''add_page() takes a category, title, url and view
       as input. If view is not provided it is defaulted to '0'
       The page object is returned with the a boolean if the object was created or not.
    '''
    page = Page.objects.get_or_create(category=cat,title=title, url=url, views=views)[0]
    return page

def add_cat(name, views, likes):
    '''add_cat() takes the category name as input.
       The category object is returned with the a boolean if the object was created or not.
    '''
    category = Category.objects.get_or_create(name=name)[0]
    category.views = views
    category.likes = likes
    category.save()
    return category


if __name__ == '__main__':
    print('Starting the Rango population script ...'
          '\nand that its what is in the data base')
    populate()