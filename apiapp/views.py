# example/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

from .serializers import CoffeeSerializer, BrandSerializer, RoastTypeSerializer
from .models import RoastType, Brand, Coffee

class BrandViewSet(viewsets.ModelViewSet):
    queryset=Brand.objects.all()
    serializer_class= BrandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RoastTypeViewSet(viewsets.ModelViewSet):
    queryset=RoastType.objects.all()
    serializer_class=RoastTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    
class CoffeeViewSet(viewsets.ModelViewSet):
    queryset=Coffee.objects.all()
    serializer_class=CoffeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]