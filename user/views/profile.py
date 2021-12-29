from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView

from ..serializers import ProfileSZ


class UserRetrieveUpdate(RetrieveUpdateAPIView):
    serializer_class = ProfileSZ
    http_method_names = ['get', 'patch']

    def get_object(self):
        return self.request.user

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: ProfileSZ})
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        return Response(data=serializer.data, status=200)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: ProfileSZ})
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
