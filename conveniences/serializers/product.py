from rest_framework import serializers

from ..models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "conveniences_store", "title", "price", "sale_type",
                  "image", "created_at")
