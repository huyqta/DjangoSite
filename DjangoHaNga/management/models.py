import uuid
from django.db import models
from management import enums


# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cat_name = models.CharField(max_length=255)    
    cat_parent = models.ForeignKey('self',default=uuid.uuid4, editable=False, unique=True)
    description = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.cat_name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category)
    description = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.product_name


#class Product(models.Model):
#    product_name = models.CharField(max_length=500, verbose_name="Product name")
#    product_title = models.CharField(max_length=500, verbose_name="Product title")
#    release_date = models.DateField(verbose_name="Release date")
#    host_address = models.CharField(max_length=500, verbose_name="Host", blank=True)
#    domain_address = models.CharField(max_length=500, verbose_name="Domain", blank=True)
#    introduction = models.CharField(max_length=500, verbose_name="Introduction", blank=True)
#    product_type = models.CharField(max_length=255, choices=enums.ListEnums.PRODUCT_TYPES, verbose_name="Type")
#    active = models.BooleanField(verbose_name="Active")

#    class Meta:
#        ordering = ["release_date"]
#        pass

#    def __unicode__(self):
#        return self.product_name


class Service(models.Model):
    Id = models.UUIDField(primary_key=True)
    Name = models.CharField(max_length=255, verbose_name="Service name")
    Code = models.CharField(max_length=255, verbose_name="Service code")
    Description = models.TextField(verbose_name="Description", blank=True)
    HostAddress = models.CharField(max_length=255, verbose_name="Host address")
    DomainAddress = models.CharField(max_length=255, verbose_name="Domain address")
    Active = models.BooleanField(verbose_name="Active service")
    ReleaseDate = models.DateTimeField(verbose_name="Release date")

#    class Meta:
#        ordering = ["Active", "Name", "ReleaseDate"]
#        pass


class Project(models.Model):
    Id = models.UUIDField(primary_key=True)
    Name = models.CharField(max_length=255, verbose_name="Project name")
    Code = models.CharField(max_length=255, verbose_name="Project code")
    Description = models.TextField(verbose_name="Description", blank=True)
    ImageUrl = models.CharField(max_length=255, verbose_name="Image url")
    ThumbImageUrl = models.CharField(max_length=255, verbose_name="Thumb image url")
    ReleaseUrl = models.CharField(max_length=255, verbose_name="Release url")
    TeamSize = models.CharField(max_length=255, verbose_name="Team size")
    StartDate = models.DateTimeField(verbose_name="Start date")
    CloseDate = models.DateTimeField(verbose_name="Close date")
    Status = models.CharField(max_length=255, choices=enums.ListEnums.STATUS_ENUM, verbose_name="Status")
    Active = models.BooleanField(verbose_name="Active service")
    ReleaseDate = models.DateTimeField(verbose_name="Release date")

    #class Meta:
    #    ordering = ["Active", "Name", "ReleaseDate"]