from django.urls import path

from . import views

app_name = 'purchases'

urlpatterns = [
    path('ready/', views.purchase_ready, name='ready'),
    path('approve/', views.purchase_approve, name='approve')
]
