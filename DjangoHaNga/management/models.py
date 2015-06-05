from django.db import models

# Create your models here.
class Categorie(models.Model):
    code = models.CharField(max_length=255, verbose_name="Category Code")
    name = models.CharField(max_length=255, verbose_name="Category Name")
    description = models.CharField(max_length=255, verbose_name="Description")

    def __unicode__(self):
        return u'%s %s' % (self.code, self.name)

class ModelTest(models.Model):
    field1Test = models.CharField(max_length=255)
    field12est = models.CharField(max_length=255, verbose_name="field 2 test")
    field13est = models.CharField(max_length=255)
