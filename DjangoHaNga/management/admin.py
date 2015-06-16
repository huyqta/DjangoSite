from django.contrib import admin

from management.models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "product_title", "release_date", "host_address", "domain_address", "introduction",
                    "product_type"]
    fields = ["product_name", "product_title", "release_date", "host_address", "domain_address", "introduction",
              "product_type"]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

