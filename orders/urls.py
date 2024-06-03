from django.urls import path
from .views import create_order, all_orders_page, my_orders_page

app_name = 'orders'
urlpatterns = [
    path('create-order/<slug:slug>', create_order, name='create_order'),
    path('all-orders/', all_orders_page, name='all-orders'),
    path('my-orders/', my_orders_page, name='my-orders'),
]