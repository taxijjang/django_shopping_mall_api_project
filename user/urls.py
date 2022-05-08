from django.urls import path

from .views import CustomTokenObtainPairView
from .views import CustomTokenRefreshView
from .views import UserSignUpCreateAV
from .views import UserRetrieveUpdate
from .views import celery_test_view

app_name = 'users'

urlpatterns = [
    path('', UserRetrieveUpdate.as_view(), name='profile'),
    path('signup/', UserSignUpCreateAV.as_view(), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', CustomTokenRefreshView.as_view(), name='login_refresh'),
    # path('test/', celery_test_view),
]
