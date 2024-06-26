from apiapp.views import BrandViewSet, RoastTypeViewSet, CoffeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet, basename='brand')
router.register(r'roast-types', RoastTypeViewSet, basename='roast-type')
router.register(r'coffee', CoffeeViewSet, basename='coffee')

urlpatterns = router.urls