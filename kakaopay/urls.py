from django.urls import path

from .views import index

app_name = 'kakaopay'

urlpatterns = [
    path('', index),
]
