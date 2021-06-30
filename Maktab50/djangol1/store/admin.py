from django.contrib import admin
from . import models


class OrderItemInline(admin.TabularInline):
    """
    Admin inline OrderItem model
    """
    model = models.OrderItem
    # fields = (
    #     'product',
    #     'qty',
    #     'price'
    # )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (
        OrderItemInline,
    )
    list_per_page = 3
    list_display = (
        'owner',
        'status',
        'created_on',
      )
    search_fields = (
        'id',
    )
    list_filter = (
        'status',
    )
    list_display_links = (
        'owner',
        'status',
    )
