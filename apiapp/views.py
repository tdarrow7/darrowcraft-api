# example/views.py
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import CoffeeSerializer, BrandSerializer, RoastTypeSerializer
from .models import RoastType, Brand, Coffee

class BrandViewSet(viewsets.ModelViewSet):
    queryset=Brand.objects.all()
    serializer_class= BrandSerializer
    
class RoastTypeViewSet(viewsets.ModelViewSet):
    queryset=RoastType.objects.all()
    serializer_class=RoastTypeSerializer


    
class CoffeeViewSet(viewsets.ModelViewSet):
    queryset=Coffee.objects.all()
    serializer_class=CoffeeSerializer