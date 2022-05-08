from rest_framework import serializers


class ReadyRequestSerializer(serializers.Serializer):
    product_pk = serializers.IntegerField()
    quantity = serializers.IntegerField()


class ReadyResponseSerializer(serializers.Serializer):
    next_redirect_pr_url = serializers.CharField()
