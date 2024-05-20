from django.contrib import admin

from orders.models import OrderItem, Order
from products.models import Product, Category
from users.models import UserProfile

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(UserProfile)
