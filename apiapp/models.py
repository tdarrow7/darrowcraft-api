import uuid
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
    name = CharField(max_length=36)
    isground = BooleanField()
    dateadded = models.DateTimeField(auto_now=True)
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, related_name='coffees')
    roasttype = models.ForeignKey("RoastType", on_delete=models.CASCADE, related_name='coffees')
    description = models.TextField(max_length=512)
    imageurl = models.TextField(max_length=128, null=True)
    slug = models.fields.SlugField
    def __str__(self) -> str:
        return self.name

class RoastType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=36)
    description = models.CharField(max_length=1024, null=True)
    dateadded = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name
    
class StackType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=36)
    def __str__(self) -> str:
        return self.name
    
class CodeProject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=72)
    link = models.CharField(max_length=128, null=True)
    description = models.CharField(max_length=1024, null=True)
    languages = models.CharField(max_length=128, null=True)
    github = models.CharField(max_length=128, null=True)
    dateadded = models.DateTimeField(auto_now=True)
    stacktype= models.ForeignKey("StackType", on_delete=models.DO_NOTHING, related_name="codeprojects")
    
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=True)
    session = models.ForeignKey("Session", on_delete=models.CASCADE, related_name="cart")
    

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE, related_name="cartitems")
    coffee = models.ForeignKey("Coffee", on_delete=models.CASCADE, related_name="cartitems")
    quantity = models.IntegerField()

class Session(models.Model):
    id = models.AutoField(primary_key=True)
    datecreated=models.DateTimeField(auto_now=True)
    active = models.BooleanField(null=True)
