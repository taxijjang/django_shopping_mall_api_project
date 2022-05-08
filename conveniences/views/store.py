# from rest_framework import generics, permissions
# from drf_spectacular.utils import extend_schema
#
# from ..models import Store
# from ..serializers import StoreListSerializer
#
#
# class StoreListView(generics.ListAPIView):
#     permission_classes = (permissions.AllowAny,)
#     queryset = Store.objects.all()
#     serializer_class = StoreListSerializer
#     pagination_class = None
#
#     @extend_schema(
#         tags=["편의점"],
#         summary="편의점 브랜드를 조회하는 API",
#     )
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)
