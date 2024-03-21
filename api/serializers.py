from rest_framework import serializers

from django.contrib.auth.models import User

from .models import (
    Category,Product,
    Client
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
                
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
    def to_representation(self,instance):
        representation = super().to_representation(instance)
        representation['fullname'] = instance.user.first_name + ' ' + instance.user.last_name
        representation['email'] = instance.user.email
        return representation
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
        extra_kwargs = {'password':{'write_only':True}}
        
    def create(self,validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user