from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Coffee, RoastType, Brand

class CoffeeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Coffee
        fields = '__all__'

class RoastTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = RoastType
        fields = '__all__'

class BrandSerializer(HyperlinkedModelSerializer):
    class Meta:     
        model = Brand
        fields = '__all__'