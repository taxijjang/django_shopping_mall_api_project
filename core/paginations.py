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

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'page_data': {
                    'type': 'object',
                    'properties': {
                        'next': {
                            'type': 'string',
                            'example': 'http://211.202.74.84/api/conveniences/products/?page=3'
                        },
                        'previous': {
                            'type': 'string',
                            'example': "http://211.202.74.84/api/conveniences/products/?page=1"
                        },
                        'page': {
                            'type': 'integer',
                            'example': 1
                        },
                        'size': {
                            'type': 'integer',
                            'example': 10,
                        },
                    },
                },
                'data': schema
            }
        }
