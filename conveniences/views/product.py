from rest_framework import generics

from ..models import Product
from ..serializers import ProductListSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        store = self.request.GET.get("store")
        title = self.request.GET.get("title")
        if store:
            queryset = queryset.filter(conveniences_store=store)
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset
