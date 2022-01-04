from rest_framework import serializers

from ..models import Product


class ProductListSZ(serializers.ModelSerializer):
    id = serializers.CharField(required=True, help_text='상품 id')

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'image',)
        read_only_fields = ('id',)


class ProductCreateSZ(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'image',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


class ProductUpdateRequestSZ(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
    image = serializers.ImageField(required=False, use_url=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'image',)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


class ProductResponseSZ(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True, help_text='상품 id')

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'image',)
        read_only_field = ('id', 'title', 'price', 'image',)
