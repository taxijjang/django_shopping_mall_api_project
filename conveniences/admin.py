from django.contrib import admin

from .models import Product
from .models import Store


@admin.register(Store)
class Store(admin.ModelAdmin):
    list_display = ("title",)
    fields = ("title",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("conveniences_store", "sale_type", "title", "price")
    fields = ("conveniences_store", "sale_type", "title", "price", "image")
    search_fields = ("title",)
