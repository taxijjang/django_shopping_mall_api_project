from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("conveniences_store", "sale_type", "title", "price")
    fields = ("conveniences_store", "sale_type", "title", "price", "image")
    search_fields = ("title",)