"""Production app models"""
import datetime
import uuid

from django.db import models
from django.utils import timezone
from django.contrib import admin

from apps.category.models import Category


def item_directory_path(instance, filename):
    return f'item/{instance.slug}/{filename}'


def product_directory_path(instance, filename):
    return f'product/{instance.slug}/{filename}'


class Item(models.Model):

    uid = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=300)
    thumbnail = models.ImageField(upload_to=item_directory_path)
    price = models.DecimalField(
        max_digits=11, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    measurement_unit = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        return ''

    @admin.display(
        boolean=True,
        ordering='added',
        description='Added recently?',
    )
    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.added <= now


class Product(models.Model):

    uid = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=300)
    thumbnail = models.ImageField(upload_to=product_directory_path)
    price = models.DecimalField(
        max_digits=11, decimal_places=2, blank=True, null=True)
    units = models.PositiveIntegerField()
    composition = models.ManyToManyField(Item, through='Component')
    # Cost of producing a unit, based on items and other related parameters
    # product_cost =
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        return ''

    @admin.display(
        boolean=True,
        ordering='added',
        description='Added recently?',
    )
    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.added <= now


class Component(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.product.name}__{self.item.name}__relation'


class Production(models.Model):

    uid = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True)
    products = models.ManyToManyField(Product, through='ProductionDetail')
    # total production cost
    date = models.DateTimeField(auto_now_add=True)

    @admin.display(
        boolean=True,
        ordering='added',
        description='Added recently?',
    )
    def was_added_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.added <= now


class ProductionDetail(models.Model):

    production = models.ForeignKey(Production, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    produced_units = models.PositiveIntegerField()
    # production cost

    def __str__(self):
        return f'production_{self.production.uid}__{self.product.name}__detail'
