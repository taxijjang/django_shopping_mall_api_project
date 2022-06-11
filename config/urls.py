from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.urls import include

from rest_framework import permissions
from strawberry_django_jwt.decorators import jwt_cookie
from strawberry_django_jwt.views import StatusHandlingGraphQLView as GQLView

from config.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    # api
    path("api/", include("api.urls"), name="api"),
    # graphql
    re_path(r'^graphql/?$', jwt_cookie(GQLView.as_view(schema=schema))),
    # prometheus
    path('', include('django_prometheus.urls')),
]

# schema_view = get_schema_view(
#     openapi.Info(
#         title="결제프로젝트 API",
#         default_version='v1',
#         description="각각의 API 테스트를 진행하기 위해서는 login을 진행한 후 생성되는 access token를 아래의 Authorize에 \n"
#                     "Bearer {발급 받은 access token}을 입력해 주세요.\n"
#                     "ex - Bearer eyJ0eXAiOiJKV1QiLC...b0eVGuJMvAvjpk-Qo\n"
#                     "login API를 제외한 나머지는 모두 인증 상태가 완료 된 이후에 사용 가능 합니다.",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="taxijjang@gmail.com"),
#         license=openapi.License(name="BSD License"),
#
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )
#
# if settings.DEBUG:
#     urlpatterns += [
#         re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
