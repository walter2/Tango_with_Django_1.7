from django import forms
from rango.models import Category, Page


class CategoryForm(forms.ModelForm):
    '''CategoryForm() defines the form for the category definition with
       the visible fields 'name'. 'views', 'likes' and the slug are
       hidden fields.
    '''
    name = forms.CharField(max_length=128, help_text='Please enter the category name.')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        '''Meta() linkes the CategoryClass to the Category model.'''
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    '''PageForm() defines the form for the page definition with title and url.'''
    title = forms.CharField(max_length=128, help_text='Please enter the title of the page.')
    url = forms.URLField(max_length=200, help_text='Please enter the URL of the page.')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        '''Meta() linkes the PageClass to the Page model.'''
        model = Page
        exclude = ('category',)
