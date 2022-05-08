from rest_framework.parsers import FormParser
from rest_framework.parsers import MultiPartParser
from rest_framework.generics import ListAPIView
from elasticsearch import Elasticsearch

from core.paginations import CustomPagination

from products.models import Product
from products.serializers import ProductListSZ


class SearchListView(ListAPIView):
    pagination_class = CustomPagination
    queryset = Product.objects.all()
    serializer_class = ProductListSZ
    http_method_names = ['get']
    parser_classes = (MultiPartParser, FormParser)

    # swagger query parameter
    # query = openapi.Parameter(
    #     'query', openapi.IN_QUERY,
    #     description='상품 검색할 내용',
    #     required=False,
    #     type=openapi.TYPE_STRING
    # )

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        return Product.objects.filter(title__icontains=query)

    # @swagger_auto_schema(
    #     operation_description='상품 검색 목록 API',
    #     manual_parameters=[
    #         query,
    #         openapi.Parameter(
    #             'Authorization',
    #             openapi.IN_HEADER,
    #             description="Bearer {token}",
    #             type=openapi.TYPE_STRING
    #         )
    #     ],
    #     paginator_inspectors=[CustomPaginatorInspectorClass],
    # )
    def get(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.get_queryset())
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(data=serializer.data)

# class SearchLiseView(APIView):
#     """
#     TODO: elasticsearch를 이용해서 검색 구현 진행
#     """
# def get(self, request):
#     es = Elasticsearch([
#         {
#             'host': 'localhost',
#             'port': '9200',
#         }
#     ])
#
#     # 검색어
#     search_word = request.query_params.get('search')
#
#     if not search_word:
#         return Response(
#             status=status.HTTP_400_BAD_REQUEST,
#             data={'message': 'search word param is missing'}
#         )
#
#     docs = es.search(
#         index='dev',
#         doc_type='products',
#         body={
#             "query": {
#                 "match": {
#                     "title": search_word
#                 }
#             }
#         }
#     )
#     data_list = docs['hits']
#     return Response(data_list)
