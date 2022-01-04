# python import
# django import
# third party import
from rest_framework.exceptions import APIException


# local import

class IncorrectUserException(APIException):
    status_code = 403
    default_detail = "올바르지 않은 유저 입니다. 확인 후 다시 요청해 주세요"
