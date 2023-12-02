from django.db import models


class CoffeeShop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    coffee_shop_id = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    rating = models.PositiveIntegerField()  # You can add constraints like max_value if you have a rating system
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.coffee_shop.name} - {self.created_at.strftime('%Y-%m-%d')}"

class CoffeeShopImage(models.Model):
    id = models.AutoField(primary_key=True)
    coffee_shop_id = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE, related_name='images')
    picture = models.ImageField(upload_to='coffeeshop_pictures/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.coffee_shop.name} Image - {self.uploaded_at.strftime('%Y-%m-%d')}"

# class Comment(models.Model):
#     coffee_shop_id = models.ForeignKey(CoffeeShop, on_delete=models.CASCADE, related_name='comments')
#     comment_text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Comment on {self.coffee_shop.name} - {self.created_at.strftime('%Y-%m-%d')}"
