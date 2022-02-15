from django.contrib import admin
from .models import Purchase
from .models import PurchaseApprovalResult


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity', 'ready', 'approve', ]


@admin.register(PurchaseApprovalResult)
class PurchaseApprovalResult(admin.ModelAdmin):
    list_display = ['id', 'purchase', 'payment_type', ]
    pass
