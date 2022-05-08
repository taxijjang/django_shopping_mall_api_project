# python import
from collections import OrderedDict
# django import
# third party import
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


# local import

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'

    def page_data_format(self, next, previous, page, size):
        page_data = dict(
            next=next,
            previous=previous,
            page=page,
            size=size,
        )
        return page_data

    def get_paginated_response(self, data):
        page_data = self.page_data_format(
            next=self.get_next_link(),
            previous=self.get_previous_link(),
            page=self.request.GET.get('page', 1),
            size=self.page.paginator.per_page,
        )
        return Response(OrderedDict((
            ('page_data', page_data),
            ('data', data),
        )))


# class CustomPaginatorInspectorClass(PaginatorInspector):
#     def get_paginated_response(self, paginator, response_schema):
#         """
#         :param BasePagination paginator: the paginator
#         :param openapi.Schema response_schema: the response schema that must be paged.
#         :rtype: openapi.Schema
#         """
#         return openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties=OrderedDict((
#                 ('next', openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, description='다음 페이지 주소')),
#                 ('previous',
#                  openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, description='이전 페이지 주소')),
#                 ('page', openapi.Schema(type=openapi.TYPE_INTEGER, description='현재 페이지 번호')),
#                 ('size', openapi.Schema(type=openapi.TYPE_INTEGER, description='한 페이지에 포함되는 아이템 수')),
#                 ('data', response_schema),
#             )),
#             required=['next', 'previous', 'page', 'size', 'data', ],
#         )
