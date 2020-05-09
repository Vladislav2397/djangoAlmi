from django.shortcuts import render
from django.views import generic
from .models import Category, Product, News


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


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class IndexListView(generic.ListView):
    model = Category
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all()
        context['products'] = [
            product for product in Product.objects.all()
            if product.isTop
        ]
        context['last_added'] = Product.objects.order_by('-pub_date')[:5]
        return context
