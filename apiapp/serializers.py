from rest_framework.serializers import HyperlinkedModelSerializer, ReadOnlyField, SlugRelatedField
from .models import CodeProject, Coffee, RoastType, Brand, StackType

class CoffeeSerializer(HyperlinkedModelSerializer):
    roasttype = SlugRelatedField(
        slug_field='name',
        queryset=RoastType.objects.all()
    )
    brand = SlugRelatedField(
        slug_field='name',
        queryset=Brand.objects.all()
    )
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
    stacktype = SlugRelatedField(
        slug_field='name',
        queryset=StackType.objects.all()
    )
    class Meta:
        model = CodeProject
        fields = ['id', 'url', 'name', 'link', 'description', 'languages', 'dateadded', 'github', 'stacktype' ]