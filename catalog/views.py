from django.shortcuts import render
from django.views import generic
from .models import Category


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'catalog/catalog.html'