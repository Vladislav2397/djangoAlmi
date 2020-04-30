from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'isMain', 'isPackage']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = [
        ('title', 'category'),
        'description',
        ('body', 'producer', 'price'),
        ('image', 'analog')
    ]
    list_display = ['title', 'category', 'price']
