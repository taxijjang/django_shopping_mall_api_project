from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from ..models import User
from ..serializers import UserSignupSZ


class UserSignUpCreateAV(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSZ
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(data=serializer.errors, status=400)
