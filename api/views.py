from rest_framework import generics

from .models import (
    Category,Product
)

from .serializers import (
    CategorySerializer,
    ProductSerializer
)

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    