from django.contrib import admin
from management.models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "product_title", "release_date", "host_address", "introduction"]
    fields = ["product_name", "product_title"]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

