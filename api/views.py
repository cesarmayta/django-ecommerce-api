from rest_framework import generics

from .models import (
    Category,Product,
    Client
)

from .serializers import (
    CategorySerializer,
    ProductSerializer,
    CategoryProductSerializer,
    ClientSerializer,
    UserSerializer
)

from django.contrib.auth.models import User

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryProductsView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    lookup_url_kwarg = 'category_id'
    serializer_class = CategoryProductSerializer
    
class ClientView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    