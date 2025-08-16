from django.contrib import admin
from django.contrib.admin.decorators import register

from products.models import Product


@register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",

    )
    list_per_page = 20

