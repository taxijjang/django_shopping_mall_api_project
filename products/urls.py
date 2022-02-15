from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListCreateAV.as_view(), name='product_list_create'),
    path('<int:pk>/', views.ProductRetrieveUpdateDestroyAV.as_view(), name='product_update_destory'),
]
