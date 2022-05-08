from django.urls import path, include
from django.conf import settings

from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from drf_spectacular.views import SpectacularRedocView

app_name = "api"

urlpatterns = [
    # user
    path('users/', include('user.urls')),
    # product
    path('products/', include('products.urls')),
    # search
    path('searches/', include('searches.urls')),
    # kakaopay
    path('kakaopay/', include('kakaopay.urls')),
    # purchase
    path('purchases/', include('purchases.urls')),
    # diaries
    path('diaries/', include('diary.urls')),
    # 편의점
    path("conveniences/", include("conveniences.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path('schema/', SpectacularAPIView.as_view(), name='schema'),
        path('swagger/', SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger-ui'),
        path('redoc/', SpectacularRedocView.as_view(url_name='api:schema'), name='redoc'),
    ]
