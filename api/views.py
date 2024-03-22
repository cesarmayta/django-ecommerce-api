from rest_framework import generics

from .models import (
    Category,Product,
    Client,Order
)

from .serializers import (
    CategorySerializer,
    ProductSerializer,
    CategoryProductSerializer,
    ClientSerializer,
    UserSerializer,
    UserUpdateSerializer,
    ClientFullSerializer,
    OrderSerializer
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
    
class ClienteDetailView(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    
class ClientFullView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientFullSerializer
    
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    