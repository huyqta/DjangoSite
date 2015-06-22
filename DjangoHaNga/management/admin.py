from django.contrib import admin

from management.models import Category, Product, Service, Project


class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "product_title", "release_date", "host_address", "domain_address", "introduction",
                    "product_type", "active"]
    fields = ["product_name", "product_title", "release_date", "host_address", "domain_address", "introduction",
              "product_type", "active"]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["Name", "Code", "Description", "HostAddress", "DomainAddress", "Active",
                    "ReleaseDate"]
    fields = ["Name", "Code", "Description", "HostAddress", "DomainAddress", "Active",
                    "ReleaseDate"]


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["Name", "Code", "Description", "ImageUrl", "ThumbImageUrl", "ReleaseUrl",
                    "TeamSize", "StartDate", "CloseDate", "Status", "Active", "ReleaseDate"]
    fields = ["Name", "Code", "Description", "ImageUrl", "ThumbImageUrl", "ReleaseUrl",
                    "TeamSize", "StartDate", "CloseDate", "Status", "Active", "ReleaseDate"]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Project, ProjectAdmin)

