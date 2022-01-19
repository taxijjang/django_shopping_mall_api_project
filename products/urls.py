from django.urls import path

from .views import ProductListCreateAV
from .views import ProductRetrieveUpdateDestroyAV

app_name = 'products'

urlpatterns = [
    path('', ProductListCreateAV.as_view(), name='product_list_create'),
    path('<int:pk>/', ProductRetrieveUpdateDestroyAV.as_view(), name='product_update_destory'),
]
