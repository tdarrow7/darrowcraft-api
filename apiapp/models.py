from django.db import models
from django.db.models.fields import CharField, AutoField, BooleanField

# Create your models here.

class Brand(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=36)
    description = models.CharField(max_length=1024, null=True)
    dateadded = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name

class Coffee(models.Model): 
    id = AutoField(primary_key=True)
    type = CharField(max_length=36)
    isground = BooleanField()
    dateadded = models.DateTimeField(auto_now=True)
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, related_name='coffees')
    roasttype = models.ForeignKey("RoastType", on_delete=models.CASCADE, related_name='coffees')
    description = models.TextField(max_length=512)
    imageurl = models.TextField(max_length=128, null=True)

class RoastType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=36)
    description = models.CharField(max_length=1024, null=True)
    dateadded = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name