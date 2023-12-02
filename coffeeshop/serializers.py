from rest_framework import serializers
from .models import CoffeeShop, Review, CoffeeShopImage


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','coffee_shop_id', 'review_text', 'rating', 'created_at']

class CoffeeShopImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeShopImage
        fields = ['id', 'coffee_shop_id','picture', 'uploaded_at']

class CoffeeShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeShop
        fields = ['id', 'name', 'address']

    
class CoffeeShopPreviewSerializer(serializers.ModelSerializer):
    images = CoffeeShopImageSerializer(many=True, read_only=True)

    class Meta:
        model = CoffeeShop
        fields = ['id', 'name', 'address', 'images']

class DetailedCoffeeShopSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    images = CoffeeShopImageSerializer(many=True, read_only=True)

    class Meta:
        model = CoffeeShop
        fields = ['id', 'name', 'address', 'reviews', 'images']