# python import
from collections import OrderedDict
# django import
from django.core.paginator import InvalidPage
# third party import
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


# local import

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'

    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = self.get_page_number(request, paginator)

        try:
            self.page = paginator.page(page_number)
        except InvalidPage as exc:
            return list()

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request
        return list(self.page)

    def page_data_format(self, next, previous, page, size, max_page):
        page_data = dict(
            next=next,
            previous=previous,
            page=page,
            size=size,
            max_page=max_page,
        )
        return page_data

    def get_paginated_response(self, data):
        if hasattr(self, 'page') and self.page is not None:
            page_data = self.page_data_format(
                next=self.get_next_link(),
                previous=self.get_previous_link(),
                page=self.request.GET.get('page', 1),
                size=self.page.paginator.per_page,
                max_page=self.page.paginator.num_pages,
            )
        else:
            page_data = self.page_data_format(
                next=None,
                previous=None,
                page=1,
                size=10,
                max_page=0,
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
                        'max_page': {
                            'type': 'integer',
                            'example': 10,
                        }
                    },
                },
                'data': schema
            }
        }
