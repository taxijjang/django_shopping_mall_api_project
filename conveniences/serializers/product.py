from rest_framework import serializers

from ..models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "store", "title", "price", "sale_type",
                  "image", "created_at")
