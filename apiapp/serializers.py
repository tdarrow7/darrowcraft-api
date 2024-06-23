from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Coffee, RoastType, Brand

class CoffeeSerializer(ModelSerializer):
    class Meta:
        model = Coffee
        fields = '__all__'

class RoastTypeSerializer(ModelSerializer):
    class Meta:
        model = RoastType
        fields = '__all__'

class BrandSerializer(ModelSerializer):
    class Meta:     
        model = Brand
        fields = '__all__'