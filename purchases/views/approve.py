from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework import decorators
from rest_framework.response import Response

from kakaopay.payment import KakaoPayClient


@swagger_auto_schema(
    method='get',
    deprecated=True,
    operation_description='카카오페이 상품 승인 - 서버에서만 사용하는 API',
)
@decorators.api_view(http_method_names=['GET'])
def kakaopay_approve(request, *args, **kwargs):
    kakaopay = KakaoPayClient()

    purchase_pk = kwargs.get('purchase_pk')
    pg_token = request.GET.get('pg_token')
    try:
        kakaopay.approve(pg_token=pg_token, purchase_pk=purchase_pk)
    except Exception as e:
        return Response(data='거래 승인 오류 발생', status=500)
    return Response(data='OK', status=200)