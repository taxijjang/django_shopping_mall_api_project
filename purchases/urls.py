from django.urls import path

from . import views

app_name = 'purchases'

urlpatterns = [
    path('ready/', views.kakaopay_ready, name='kakaopay_ready'),
    path('approve/<int:purchase_pk>/', views.kakaopay_approve, name='kakaopay_approve')
]
