from django.urls import path, include

urlpatterns = [
    path("conveniences/", include("conveniences.urls")),
]
