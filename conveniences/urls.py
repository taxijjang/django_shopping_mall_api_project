from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.ProductListView.as_view(), name="products"),
    path("products/similars/", views.SimilarProductListView.as_view(), name="product_similars"),
]
