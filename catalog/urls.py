from django.urls import path
from .views import (
    CategoryListView, CategoryDetailView,
    ProductDetailView, IndexListView
)

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('catalog/', CategoryListView.as_view(), name='category'),

    path(
        'catalog/<int:pk>',
        CategoryDetailView.as_view(),
        name='category-table'
    ),

    path(
        'product/<int:pk>',
        ProductDetailView.as_view(),
        name='product-detail'
    ),
]
