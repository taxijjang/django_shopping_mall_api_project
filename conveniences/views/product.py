from django.utils import timezone
from django.db.models import Q

from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

from ..models import Product
from ..serializers import ProductListSerializer


class ProductListView(generics.ListAPIView):
    """
    ### 할인 타입
    - 1+1
    - 2+1
    - 3+1
    - 4+1
    - 할인상품
    - 증정상품

    ### 편의점 종류
    - cu
    - emart24
    - seven_eleven
    - gs25
    - ministop
    """
    permission_classes = (permissions.AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        store = self.request.GET.get("store")
        title = self.request.GET.get("title")
        sale_type = self.request.GET.get("sale_type")
        order = self.request.GET.get("order")
        year = self.request.GET.get("year", timezone.now().year)
        month = self.request.GET.get("month", timezone.now().month)
        favorites = self.request.query_params.getlist('favorites')
        if store:
            queryset = queryset.filter(store=store)
        if title:
            queryset = queryset.filter(title__icontains=title)

        if sale_type:
            queryset = queryset.filter(sale_type=sale_type)

        if favorites:
            favorite_list = favorites[0].split(',')
            result_favorite = Q()
            for favorite in favorite_list:
                result_favorite |= Q(title=favorite)
            queryset = queryset.filter(result_favorite)
        # 날짜 필터링
        queryset = queryset.filter(
            Q(year=year)
            & Q(month=month)
        )
        if order:
            queryset = queryset.order_by(order)
        queryset = queryset.exclude(sale_type=Product.SALE_PRODUCT).exclude(sale_type=Product.PRESENT_PRODUCT)
        return queryset

    @extend_schema(
        summary="편의점 할인 상품 정보를 제공하는 API",
        tags=["편의점"],
        parameters=[
            OpenApiParameter(
                "store",
                OpenApiTypes.STR,
                OpenApiParameter.QUERY,
                description="편의점 종류",
                enum=["cu", "emart24", "seven_eleven", "gs25"],
            ),
            OpenApiParameter(
                "title",
                OpenApiTypes.STR,
                OpenApiParameter.QUERY,
                description="검색하려는 상품 이름\n\nex) 상품이름1",
            ),
            OpenApiParameter(
                "favorites",
                OpenApiTypes.STR,
                OpenApiParameter.QUERY,
                description="즐겨 찾는 상품 목록\n\nex) 상품이름1,상품이름2",
            ),
            OpenApiParameter(
                "sale_type",
                OpenApiTypes.STR,
                OpenApiParameter.QUERY,
                description="할인 타입",
                # enum=["1+1", "2+1", "3+1", "4+1", "할인상품", "증정상품"],
                enum=["1+1", "2+1", "3+1", "4+1"],
            ),
            OpenApiParameter(
                "order",
                OpenApiTypes.STR,
                OpenApiParameter.QUERY,
                description="정렬 방법",
                enum=["price", "-price", ]
            ),
            OpenApiParameter(
                "year",
                OpenApiTypes.STR,
                OpenApiParameter.QUERY,
                description="할인 연도\n\nex) 2022",
            ),
            OpenApiParameter(
                "month",
                OpenApiTypes.STR,
                OpenApiParameter.QUERY,
                description="할인 월\n\nex) 1",
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
