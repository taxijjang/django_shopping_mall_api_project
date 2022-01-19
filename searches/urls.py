from django.urls import path

from .views import SearchListView

app_name = 'search'

urlpatterns = [
    path('', SearchListView.as_view(), name='search')
]