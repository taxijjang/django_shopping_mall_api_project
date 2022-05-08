from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView

from core.renderers import CustomRenderer
from ..serializers import ProfileSZ


class UserRetrieveUpdate(RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ProfileSZ
    http_method_names = ['get', 'patch']

    def get_object(self):
        return self.request.user

    # @swagger_auto_schema(
    #     operation_description='access token을 이용하여\n나의 정보 확인 API',
    #     manual_parameters=[
    #         openapi.Parameter(
    #             'Authorization',
    #             openapi.IN_HEADER,
    #             description="Bearer {token}",
    #             type=openapi.TYPE_STRING
    #         )
    #     ]
    # )
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return Response(data=serializer.data, status=200)

    # @swagger_auto_schema(
    #     responses={
    #         status.HTTP_200_OK: ProfileSZ
    #     },
    #     operation_description='access token을 이용하여\n나의 정보 수정 API',
    #     manual_parameters=[
    #         openapi.Parameter(
    #             'Authorization',
    #             openapi.IN_HEADER,
    #             description="Bearer {token}",
    #             type=openapi.TYPE_STRING
    #         )
    #     ]
    # )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
