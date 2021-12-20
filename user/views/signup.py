from rest_framework.generics import CreateAPIView

from ..models import User


class UserSignUpCreateAV(CreateAPIView):
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        pass
