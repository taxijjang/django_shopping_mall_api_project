from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.urls import include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('admin/', admin.site.urls),

    # user
    path('users/', include('user.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="결제프로젝트 API",
        default_version='v1',
        description="각각의 API 테스트를 진행하기 위해서는 login을 진행한 후 생성되는 access token를 아래의 Authorize에 \n"
                    "Bearer {발급 받은 access token}을 입력해 주세요.\n"
                    "ex - Bearer eyJ0eXAiOiJKV1QiLC...b0eVGuJMvAvjpk-Qo\n"
                    "login API를 제외한 나머지는 모두 인증 상태가 완료 된 이후에 사용 가능 합니다.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="taxijjang@gmail.com"),
        license=openapi.License(name="BSD License"),

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
