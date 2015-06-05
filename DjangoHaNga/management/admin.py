from django.contrib import admin
from management.models import Categorie, ModelTest

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

admin.site.register(Categorie)
admin.site.register(ModelTest)