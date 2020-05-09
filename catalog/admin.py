from django.contrib import admin
from .models import Category, Product, News


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'isMain', 'isPackage']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = [
        ('title', 'category'),
        'description',
        ('body', 'producer', 'price'),
        ('isTop', 'pub_date'),
        ('image', 'analog')
    ]
    list_display = ['title', 'category', 'price']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass
