from rest_framework import viewsets
from .models import CoffeeShop, Review, CoffeeShopImage
from .serializers import CoffeeShopSerializer, DetailedCoffeeShopSerializer,CoffeeShopPreviewSerializer, ReviewSerializer, CoffeeShopImageSerializer
from rest_framework.response import Response
from rest_framework import status

class CoffeeShopViewSet(viewsets.ModelViewSet):
    queryset = CoffeeShop.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CoffeeShopPreviewSerializer 
        elif self.action == 'retrieve':
            return DetailedCoffeeShopSerializer
        return CoffeeShopSerializer

    def create(self, request, *args, **kwargs):
        serializer = CoffeeShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = CoffeeShop.objects.all()
        name = self.request.query_params.get('name', None)
        address = self.request.query_params.get('address', None)

        if name:
            queryset = queryset.filter(name__icontains=name)
        if address:
            queryset = queryset.filter(address__icontains=address)

        return queryset
    
class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.all()
        coffee_shop_id = self.request.query_params.get('coffee_shop_id', None)

        if coffee_shop_id is not None:
            queryset = queryset.filter(coffee_shop_id=coffee_shop_id)

        return queryset

class CoffeeShopImageViewSet(viewsets.ModelViewSet):

        serializer_class = CoffeeShopImageSerializer
        def get_queryset(self):
            queryset = CoffeeShopImage.objects.all()
            coffee_shop_id = self.request.query_params.get('coffee_shop_id', None)

            if coffee_shop_id is not None:
                queryset = queryset.filter(coffee_shop_id=coffee_shop_id)

            return queryset