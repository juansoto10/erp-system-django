"""Category app models"""
import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


def category_directory_path(instance, filename):
    """Generate the file path for a Category's thumbnail.

    Args:
        instance: The Category instance.
        filename (str): The original filename of the uploaded file.

    Returns:
        str: The file path for the Category's thumbnail.
    """
    
    return f'category/{instance.slug}/{filename}'


class Category(models.Model):
    """Represents a category in the system.

    Attributes:
    - name: CharField, the name of the category.
    - slug: SlugField, a unique slug for the category.
    - thumbnail: ImageField, an image representing the category.
    - added: DateTimeField, timestamp of when the category was added.
    """

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to=category_directory_path)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the Category."""
        return self.name

    def get_thumbnail(self):
        """Returns the URL of the category's thumbnail or an empty string if no thumbnail is available."""
        if self.thumbnail:
            return self.thumbnail.url
        return ''

    @admin.display(
        boolean=True,
        ordering='published',
        description='Published recently?',
    )
    def was_added_recently(self):
        """
        Checks if the category was added recently.

        Returns:
            bool: True if the category was added within the last day, False otherwise.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.added <= now
