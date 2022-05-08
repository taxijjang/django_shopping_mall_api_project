from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.contrib.auth import get_user_model
from ..serializers import UserSignupSZ

User = get_user_model()


class UserSignUpCreateAV(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSZ
    permission_classes = [AllowAny, ]

    # @swagger_auto_schema(
    #     responses={
    #         status.HTTP_200_OK: UserSignupSZ
    #     },
    #     operation_description='회원 가입 API'
    # )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(data=serializer.errors, status=400)
