# example/views.py
from rest_framework import generics, viewsets
from rest_framework.response import Response

from .serializers import CoffeeSerializer, BrandSerializer, RoastTypeSerializer
from .models import RoastType, Brand, Coffee
from django.shortcuts import get_object_or_404, get_list_or_404

# def index(request):
#     now = datetime.now()
#     html = f'''
#     <html>
#         <body>
#             <h1>Hello from Vercelll!</h1>
#             <p>The current time is { now }.</p>
#         </body>
#     </html>
#     '''
#     return HttpResponse(html)

# Fix this, todd broke it

# class CoffeeList(viewsets.ModelViewSet):
#     queryset = Coffee.objects.all()
#     serializer = CoffeeSerializer

# class CoffeeDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Coffee.objects.all()
#     serializer_class = CoffeeSerializer

class BrandViewSet(viewsets.ViewSet):
    def list(self, request):
            queryset = Brand.objects.all()
            serializer = BrandSerializer(queryset, many=True)
            return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
            queryset = Brand.objects.all()
            brand = get_object_or_404(queryset, pk=pk)
            serializer = BrandSerializer(brand)
            return Response(serializer.data)
    
class RoastTypeViewSet(viewsets.ViewSet):
    def list(self, request):
            queryset = RoastType.objects.all()
            serializer = RoastTypeSerializer(queryset, many=True)
            return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
            queryset = RoastType.objects.all()
            roastType = get_object_or_404(queryset, pk=pk)
            serializer = RoastTypeSerializer(roastType)
            return Response(serializer.data)
    
class CoffeeViewSet(viewsets.ViewSet):
    def list(self, request):
            queryset = Coffee.objects.all()
            serializer = CoffeeSerializer(queryset, many=True)
            return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
            queryset = Coffee.objects.all()
            coffee = get_object_or_404(queryset, pk=pk)
            serializer = CoffeeSerializer(coffee)
            return Response(serializer.data)
    


# class BrandList(generics.ListCreateAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer

# # Fix this, todd broke it
# class BrandDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer

# class RoastTypeList(generics.ListCreateAPIView):
#     queryset = RoastType.objects.all()
#     serializer_class = RoastTypeSerializer

# # Fix this, todd broke it
# class RoastTypeDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = RoastType.objects.all()
#     serializer_class = RoastTypeSerializer