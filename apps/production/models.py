"""Production app models"""
import datetime
import uuid

from django.db import models
from django.utils import timezone
from django.contrib import admin

from apps.category.models import Category


def item_directory_path(instance, filename):
    """Generate the file path for an Item's thumbnail.

    Args:
        instance: The Item instance.
        filename (str): The original filename of the uploaded file.

    Returns:
        str: The file path for the Item's thumbnail.
    """
    
    return f'item/{instance.slug}/{filename}'


def product_directory_path(instance, filename):
    """Generate the file path for a Product's thumbnail.

    Args:
        instance: The Product instance.
        filename (str): The original filename of the uploaded file.

    Returns:
        str: The file path for the Product's thumbnail.
    """
    
    return f'product/{instance.slug}/{filename}'


class Item(models.Model):
    """
    Represents an individual item in the production system.

    Attributes:
    - uid: UUIDField, unique identifier for the item.
    - name: CharField, the name of the item.
    - slug: SlugField, a unique slug for the item.
    - description: CharField, a brief description of the item.
    - thumbnail: ImageField, an image representing the item.
    - price: DecimalField, the price of the item.
    - amount: DecimalField, the amount of the item.
    - measurement_unit: CharField, the unit of measurement for the item.
    - category: ForeignKey, links the item to a category.
    - added: DateTimeField, timestamp of when the item was added.
    """

    uid = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    thumbnail = models.ImageField(upload_to=item_directory_path)
    price = models.DecimalField(
        max_digits=11, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    measurement_unit = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """String representation of the Item."""
        return self.name

    def get_thumbnail(self):
        """Returns the URL of the item's thumbnail or an empty string if no thumbnail is available."""
        if self.thumbnail:
            return self.thumbnail.url
        return ''

    @admin.display(
        boolean=True,
        ordering='added',
        description='Added recently?',
    )
    def was_added_recently(self):
        """
        Checks if the item was added recently.
        
        Returns:
            bool: True if the item was added within the last day, False otherwise.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.added <= now


class Product(models.Model):
    """
    Represents a product in the production system.

    Attributes:
    - uid: UUIDField, unique identifier for the product.
    - name: CharField, the name of the product.
    - slug: SlugField, a unique slug for the product.
    - description: CharField, a brief description of the product.
    - thumbnail: ImageField, an image representing the product.
    - price: DecimalField, the price of the product.
    - units: PositiveIntegerField, the number of units of the product.
    - composition: ManyToManyField, links the product to its components.
    - category: ForeignKey, links the product to a category.
    - added: DateTimeField, timestamp of when the product was added.
    """
    
    uid = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    thumbnail = models.ImageField(upload_to=product_directory_path)
    price = models.DecimalField(
        max_digits=11, decimal_places=2, blank=True, null=True)
    units = models.PositiveIntegerField()
    composition = models.ManyToManyField(Item, through='Component')
    # Cost of producing a unit, based on items and other related parameters
    # product_cost =
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """String representation of the Product."""
        return self.name

    def get_thumbnail(self):
        """Returns the URL of the product's thumbnail or an empty string if no thumbnail is available."""
        if self.thumbnail:
            return self.thumbnail.url
        return ''

    @admin.display(
        boolean=True,
        ordering='added',
        description='Added recently?',
    )
    def was_added_recently(self):
        """
        Checks if the product was added recently.
        
        Returns:
            bool: True if the product was added within the last day, False otherwise.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.added <= now


class Component(models.Model):
    """
    Represents a component in the production system.

    Attributes:
    - uid: UUIDField, unique identifier for the component.
    - product: ForeignKey, links the component to a product.
    - item: ForeignKey, links the component to an item.
    - amount: DecimalField, the amount of the item in the component (per Kg).
    """

    uid = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True) # per Kg

    def __str__(self):
        """String representation of the Component."""
        return f'{self.product.slug}__{self.item.slug}__relation'


class Production(models.Model):
    """
    Represents a production process in the system.

    Attributes:
    - uid: UUIDField, unique identifier for the production.
    - products: ManyToManyField, links the production to its products.
    - date: DateTimeField, timestamp of when the production occurred.
    """

    uid = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True)
    products = models.ManyToManyField(Product, through='ProductionDetail')
    # total production cost
    added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        """String representation of the production"""
        return f'production_{self.uid}'

    @admin.display(
        boolean=True,
        ordering='added',
        description='Added recently?',
    )
    def was_added_recently(self):
        """
        Checks if the production was added recently.
        
        Returns:
            bool: True if the production was added within the last day, False otherwise.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.added <= now


class ProductionDetail(models.Model):
    """
    Represents the details of a production process.

    Attributes:
    - uid: UUIDField, unique identifier for the production detail.
    - production: ForeignKey, links the detail to a production.
    - product: ForeignKey, links the detail to a product.
    - produced_units: PositiveIntegerField, the number of units produced.
    """

    uid = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True)
    production = models.ForeignKey(Production, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    produced_units = models.PositiveIntegerField()
    # production cost

    def __str__(self):
        """String representation of the ProductionDetail."""
        return f'production_{self.production.uid}__{self.product.slug}_detail'
