from django.shortcuts import render
from django.views import generic
from .models import Category


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'catalog.html'


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'catalog_table.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context
