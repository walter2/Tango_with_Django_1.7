from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    '''Category() is the model for the entry category.'''
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        '''save() implements self.slug for pretty
           name URL creation.
        '''
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Page(models.Model):
    '''Page() represents the page in the database.
       It is has Category() as foreign key.
    '''
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
