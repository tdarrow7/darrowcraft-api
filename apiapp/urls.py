from apiapp.views import BrandViewSet, CartItemViewSet, CartViewSet, CodeProjectViewSet, RoastTypeViewSet, CoffeeViewSet, StackTypeViewSet, SessionViewSet, get_cart_with_items
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet, basename='brand')
router.register(r'roasttypes', RoastTypeViewSet, basename='roasttype')
router.register(r'coffee', CoffeeViewSet, basename='coffee')
router.register(r'codeprojects', CodeProjectViewSet, basename='codeproject')
router.register(r'stacktypes', StackTypeViewSet, basename='stacktype')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'cartitems', CartItemViewSet, basename='cartitems')
router.register(r'session', SessionViewSet, basename='session')

urlpatterns = [
    path('', include(router.urls)),
    path('cart-with-items/<int:cart_id>/', get_cart_with_items, name='get_cart_with_items')
]