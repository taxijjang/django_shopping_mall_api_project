from rest_framework import generics

from ..models import Diary
from ..serializers import DiarySerializer


class DiaryListCreateView(generics.ListCreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer


class DiaryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
