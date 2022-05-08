from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from ..serializers import TokenObtainPairResponseSerializer
from ..serializers import TokenRefreshResponseSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

    # @swagger_auto_schema(
    #     responses={
    #         status.HTTP_200_OK: TokenObtainPairResponseSerializer},
    #     operation_description='email, password로 jwt token 발급 API',
    # )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):
    # @swagger_auto_schema(
    #     responses={
    #         status.HTTP_200_OK: TokenRefreshResponseSerializer},
    #     operation_description='refresh token으로 jwt token 갱신 API',
    # )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
