from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

from ..models import Product
from ..serializers import ProductListSerializer


class SimilarProductListView(generics.ListAPIView):
    # TODO: ElasticSearch로 변경해서 tokenizer 해줘야댐
    permission_classes = (permissions.AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get("title")
        # queryset = queryset[:3]
        return queryset.none()

    @extend_schema(
        summary="비슷한 상품 정보를 제공하는 API",
        tags=["편의점"],
        parameters=[
            OpenApiParameter(
                "title",
                OpenApiTypes.STR,
                OpenApiParameter.QUERY,
                description="비슷한 상품을 조회하기 위한 현재 상품의 이름",
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
