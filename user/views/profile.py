from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView

from ..models import User
from ..serializers import ProfileSZ


class UserRetrieveUpdate(RetrieveUpdateAPIView):
    serializer_class = ProfileSZ

    def get_object(self):
        User.objects.get(pk=1)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: ProfileSZ})
    def get(self, request, *args, **kwargs):
        print("ABC")
        return Response(data='1', status=200)

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: ProfileSZ})
    def patch(self, request, *args, **kwargs):
        print("ABC")
        return Response(data='1', status=200)
