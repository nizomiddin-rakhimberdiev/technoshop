from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.PositiveIntegerField()
    order_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} is ordered by {self.user.username}"

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.product.price
        super().save(*args, **kwargs)



# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#
#     def __str__(self):
#         return f"{self.quantity} of {self.product.name} in Order {self.order.id}"
