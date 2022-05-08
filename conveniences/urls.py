from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.ProductListView.as_view(), name="products"),
    path("stores/", views.StoreListView.as_view(), name="stores")
]
