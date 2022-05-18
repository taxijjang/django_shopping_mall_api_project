from rest_framework import generics, permissions

from ..models import Diary
from ..serializers import DiarySerializer


class DiaryListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    pagination_class = None


class DiaryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny,]
    http_method_names = ['patch', 'delete']
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    pagination_class = None
