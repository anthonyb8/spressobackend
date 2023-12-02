from rest_framework.routers import DefaultRouter
from .views import CoffeeShopViewSet, ReviewViewSet, CoffeeShopImageViewSet
from django.contrib import admin
from django.urls import path, include

router = DefaultRouter()
router.register(r'coffeeshops', CoffeeShopViewSet, basename='coffeeshops')
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'images', CoffeeShopImageViewSet, basename='images')


urlpatterns = [
    path('', include(router.urls)),
]
