from rest_framework import generics

from ..models import Diary
from ..serializers import DiarySerializer


class DiaryListCreateView(generics.ListCreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    pagination_class = None


class DiaryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['patch', 'delete']
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    pagination_class = None
