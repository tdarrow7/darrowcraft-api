from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, ReadOnlyField, SlugRelatedField
from .models import Cart, CartItem, CodeProject, Coffee, RoastType, Brand, Session, StackType

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

class CartSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'url', 'name', 'session']

class CartItemSerializer(HyperlinkedModelSerializer):
    coffee = SlugRelatedField(
        slug_field='name',
        queryset = Coffee.objects.all()
    )
    class Meta:
        model = CartItem
        fields = ['id', 'coffee', 'cart', 'quantity' ]

class SessionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'url', 'datecreated', 'active']
