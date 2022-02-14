import requests

from rest_framework import decorators
from rest_framework.response import Response

from kakaopay.payment import KakaoPayClient
from ..models import Product


@decorators.api_view(http_method_names=['POST'])
def kakaopay_tid(request, *args, **kwargs):
    KakaoPayClient.tid()
    return Response(data='ok')