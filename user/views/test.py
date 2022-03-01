from rest_framework import decorators
from rest_framework.response import Response

from config.celery import do_calc_total


@decorators.api_view(['GET'])
def celery_test_view(request):
    hi = do_calc_total.delay()
    return Response()
