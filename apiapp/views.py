# example/views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

from .serializers import CartItemSerializer, CartSerializer, CodeProjectSerializer, CoffeeSerializer, BrandSerializer, RoastTypeSerializer, StackTypeSerializer
from .models import Cart, CartItem, CodeProject, RoastType, Brand, Coffee, StackType

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

class CodeProjectViewSet(viewsets.ModelViewSet):
    queryset=CodeProject.objects.all()
    serializer_class=CodeProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class StackTypeViewSet(viewsets.ModelViewSet):
    queryset=StackType.objects.all()
    serializer_class=StackTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class=CartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]