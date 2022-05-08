from rest_framework import decorators
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from kakaopay.payment import KakaoPayClient
from products.models import Product
from ..serializers import ReadyRequestSerializer
from ..serializers import ReadyResponseSerializer


#
# @swagger_auto_schema(
#     method='post',
#     operation_description='카카오페이로 상품 구매 준비',
#     manual_parameters=[
#         openapi.Parameter(
#             'Authorization',
#             openapi.IN_HEADER,
#             required=True,
#             description="Bearer {token}",
#             type=openapi.TYPE_STRING
#         ),
#     ],
#     request_body=openapi.Schema(
#         type=openapi.TYPE_OBJECT,
#         properties={
#             'product_pk': openapi.Schema(type=openapi.TYPE_INTEGER),
#             'quantity': openapi.Schema(type=openapi.TYPE_INTEGER),
#         }
#     ),
#     responses={
#         status.HTTP_200_OK: openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'next_redirect_pc_url': openapi.Schema(
#                     type=openapi.TYPE_STRING,
#                     format='https://mockup-pg-web.kakao.com/v1/xxxxxxxxxx/info'
#                 )
#             }
#         )
#     }
# )
@extend_schema(
    responses=ReadyResponseSerializer,
    request=ReadyRequestSerializer,
)
@decorators.api_view(http_method_names=['POST'])
@decorators.permission_classes(permission_classes=(AllowAny,))
def kakaopay_ready(request):
    kakaopay = KakaoPayClient()
    user = request.user

    product = Product.objects.get(pk=request.data.get('product_pk'))
    quantity = request.data.get('quantity', 1)
    data = kakaopay.ready(user, product, quantity=quantity)
    return Response(data=data)
