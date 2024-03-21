from rest_framework import serializers

from .models import (
    Category,Product
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
    def to_representation(self,instance):
        representation = super().to_representation(instance)
        return representation
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
    def to_representation(self,instance):
        representation = super().to_representation(instance)
        representation['image'] = instance.image.url
        return representation
    
class CategoryProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True,read_only=True)
    
    class Meta:
        model = Category
        fields = ['id','name','products']