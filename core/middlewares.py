from django.http import JsonResponse
from django.middleware.common import MiddlewareMixin


class ErrorMiddleWare(MiddlewareMixin):
    def process_exception(self, request, exception):
        # return Response(exception=exception)
        data = dict(
            error=str(exception)
        )
        return JsonResponse(data=data, status=500)
