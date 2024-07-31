# example/views.py
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import authenticate

from .serializers import CartItemSerializer, CartSerializer, CodeProjectSerializer, CoffeeSerializer, BrandSerializer, RoastTypeSerializer, SessionSerializer, StackTypeSerializer
from .models import Cart, CartItem, CodeProject, RoastType, Brand, Coffee, Session, StackType

# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             token = generate_token(user)
#             return Response({'token': token}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

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


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

