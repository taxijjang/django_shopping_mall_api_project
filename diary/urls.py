from django.urls import path

from . import views

app_name = "diary"

urlpatterns = [
    path("", views.DiaryListCreateView.as_view()),
    path("<int:pk>/", views.DiaryRetrieveUpdateDestroyView.as_view()),
]
