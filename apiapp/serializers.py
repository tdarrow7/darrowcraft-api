from rest_framework.serializers import HyperlinkedModelSerializer, ReadOnlyField
from .models import CodeProject, Coffee, RoastType, Brand, StackType

class CoffeeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Coffee
        fields = ['id', 'url', 'name', 'isground', 'description', 'dateadded', 'imageurl', 'brand', 'roasttype']

class RoastTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = RoastType
        fields = '__all__'

class BrandSerializer(HyperlinkedModelSerializer):
    class Meta:     
        model = Brand
        fields = '__all__'

class StackTypeSerializer(HyperlinkedModelSerializer):
    class Meta:     
        model = StackType
        fields = ['id', 'name']

class CodeProjectSerializer(HyperlinkedModelSerializer):
    stacktype = ReadOnlyField(source='stacktype.name')
    class Meta:
        model = CodeProject
        fields = ['id', 'url', 'name', 'link', 'description', 'languages', 'dateadded', 'github', 'stacktype' ]