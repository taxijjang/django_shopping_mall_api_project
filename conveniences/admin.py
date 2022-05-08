from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("store", "sale_type", "title", "price")
    fields = ("store", "sale_type", "title", "price", "image")
    search_fields = ("title",)
