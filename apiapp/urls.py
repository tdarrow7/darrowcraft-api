from apiapp.views import BrandViewSet, RoastTypeViewSet, CoffeeViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet, basename='brand')
router.register(r'roasttypes', RoastTypeViewSet, basename='roasttype')
router.register(r'coffee', CoffeeViewSet, basename='coffee')

urlpatterns = [
    path('', include(router.urls))
]