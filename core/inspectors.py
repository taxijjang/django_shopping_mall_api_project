# python import
from collections import OrderedDict
# django import
# third party import


# class CustomPaginatorInspectorClass(PaginatorInspector):
#     def get_paginated_response(self, paginator, response_schema):
#         """
#         :param BasePagination paginator: the paginator
#         :param openapi.Schema response_schema: the response schema that must be paged.
#         :rtype: openapi.Schema
#         """
#
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
#             required=['next', 'previous', 'page', 'size', 'data'],
#         )
