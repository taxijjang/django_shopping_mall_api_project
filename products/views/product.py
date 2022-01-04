from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from core.paginations import CustomPagination
from core.paginations import CustomPaginatorInspectorClass
from ..models import Product
from ..serializers import ProductListSZ
from ..serializers import ProductCreateSZ
from ..serializers import ProductUpdateRequestSZ
from ..serializers import ProductResponseSZ


class ProductListCreateAV(ListCreateAPIView):
    pagination_class = CustomPagination
    queryset = Product.objects.all()
    http_method_names = ['get', 'post']
    # parser_classes = (MultiPartParser, FormParser, JSONParser)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductListSZ
        elif self.request.method == 'POST':
            return ProductCreateSZ

    @swagger_auto_schema(
        operation_description='상품 목록 API',
        paginator_inspectors=[CustomPaginatorInspectorClass],
    )
    def get(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.get_queryset())
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(data=serializer.data)

    @swagger_auto_schema(
        operation_description='상품 등록 API',
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.POST)
        if serializer.is_valid():
            serializer.save(
                image=request.data.get('image')
            )
            serializer.save()
            return Response(serializer.data)
        raise ValueError()


class ProductRetrieveUpdateDestroyAV(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    http_method_names = ['get', 'patch', 'delete']
    parser_classes = (FormParser, MultiPartParser)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductListSZ
        elif self.request.method == 'PATCH':
            return ProductUpdateRequestSZ

    @swagger_auto_schema(
        operation_description='상품 detail API'
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='상품 수정 API',
        responses={
            '200': ProductResponseSZ
        }
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='상품 삭제 API'
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)