from django.contrib import admin
from rango.models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    '''CategoryAdmin() customises the category page
       in the admin view and lists all attributes of
       the category.
    '''
    #prepopulated_fields = {'slug': ('name',)} #left out for now as it did no difference in the admin view, 2014-11-07 07:14
    list_display = ('name', 'views', 'likes')


class PageAdmin(admin.ModelAdmin):
    '''PageAdmin() customises the page view
       in the admin page and lists all attributes of
       the page with the category.
    '''
    list_display = ('title', 'category', 'url', 'views')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)