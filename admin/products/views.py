from rest_framework import viewsets, status
from .models import Products, User
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .producer import publish
import random

# Create your views here.
class ProductViewSet(viewsets.ViewSet):
    def list(self, request): # /api/products
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request): # /api/products
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): # /api/products/<str:id>
        product = Products.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None): # /api/products/<str:id>
        product = Products.objects.get(id=pk)
        serializer = ProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated', serializer.data)
        return Response(serializer.data)

    def destroy(self, request, pk=None): # /api/products/<str:id>
        product = Products.objects.get(id=pk)
        publish('product_deleted', pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            "id": user.id
        })