import re
from uuid import uuid4


from django.db import models

from accounts.models import User

# Create your models here.


def upload_image(instance, filename):
    pattern = r'.*\.(png|jpg|gif)'
    filename = filename.lower()
    formats = re.findall(pattern, filename)
    return f'books_images/{uuid4()}.{formats[0]}'


class Category(models.Model):
    name = models.CharField(max_length=510, blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name

    def get_children(self):
        return Category.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.is_parent is not None:
            return False
        return True


class Book(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class Image(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(default='', upload_to=upload_image, null=True, blank=True)


class TypeDeal(models.Model):
    CHOICES = (
        ('t', 'Trade'),
        ('s', 'Sale'),
        ('g', 'Gift')
    )
    name = models.CharField(max_length=5, choices=CHOICES)


class Deal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(TypeDeal, related_name='deals', on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_created=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    archive = models.BooleanField(default=False)
