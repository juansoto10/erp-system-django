"""Category app models"""
import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


def category_directory_path(instance, filename):
    return f'category/{instance.slug}/{filename}'


class Category(models.Model):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to=category_directory_path)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        return ''

    @admin.display(
        boolean=True,
        ordering='published',
        description='Published recently?',
    )
    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.added <= now
