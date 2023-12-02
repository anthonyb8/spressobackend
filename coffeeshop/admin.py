from django.contrib import admin
from .models import CoffeeShop, CoffeeShopImage, Review

# Register your models here.
admin.site.register(CoffeeShop)
admin.site.register(Review)
admin.site.register(CoffeeShopImage)
