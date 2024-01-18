from django.contrib import admin

from .models import *


class ItemAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug', 'description', 'thumbnail', 'price', 'amount',
                    'measurement_unit', 'category', 'uid', 'added', 'was_added_recently')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    date_hierarchy = 'added'
    
class ComponentInline(admin.TabularInline):
    
    model = Component
    extra = 12

class ProductAdmin(admin.ModelAdmin):
    
    def display_composition(self, obj):
        return ', '.join([item.name for item in obj.composition.all()])

    display_composition.short_description = 'Composition'

    inlines = [ComponentInline]
    list_display = ('name', 'slug', 'description', 'thumbnail', 'price', 'units',
                    'display_composition', 'category', 'uid', 'added', 'was_added_recently')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    date_hierarchy = 'added'
    

class ProductsInline(admin.StackedInline):
    
    model = ProductionDetail
    extra = 7


class ProductionAdmin(admin.ModelAdmin):
    
    def display_products(self, obj):
        return ', '.join([product.name for product in obj.products.all()])
    
    inlines = [ProductsInline]
    display_products.short_description = 'Products'
    list_display = ('uid', 'display_products', 'added', 'was_added_recently')
    date_hierarchy = 'added'


admin.site.register(Item, ItemAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Component)
admin.site.register(Production, ProductionAdmin)
admin.site.register(ProductionDetail)
