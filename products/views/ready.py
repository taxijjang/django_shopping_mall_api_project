import requests

from rest_framework import decorators
from rest_framework.response import Response

from kakaopay.payment import KakaoPayClient
from ..models import Product


@decorators.api_view(http_method_names=['POST'])
def kakaopay_ready(request, *args, **kwargs):
    kakaopay = KakaoPayClient()
    user = request.user

    product = Product.objects.get(pk=request.data.get('product_pk'))
    quantity = request.data.get('quantity', 1)
    data = kakaopay.ready(user, product, quantity=quantity)
    return Response(data=data)