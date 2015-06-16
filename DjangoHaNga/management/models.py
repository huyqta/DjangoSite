from django.db import models

from management import enums


# Create your models here.
class Category(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Product(models.Model):
    product_name = models.CharField(max_length=500, verbose_name="Product name")
    product_title = models.CharField(max_length=500, verbose_name="Product title")
    release_date = models.DateField(verbose_name="Release date")
    host_address = models.CharField(max_length=500, verbose_name="Host", blank=True)
    domain_address = models.CharField(max_length=500, verbose_name="Domain", blank=True)
    introduction = models.CharField(max_length=500, verbose_name="Introduction", blank=True)
    product_type = models.CharField(max_length=255, choices=enums.ListEnums.PRODUCT_TYPES, verbose_name="Type")

    class Meta:
        ordering = ["release_date"]
        pass

    def __unicode__(self):
        return self.product_name

