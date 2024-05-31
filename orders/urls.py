from django.urls import path
from .views import create_order
app_name = 'orders'
urlpatterns = [
    path('create-order/<slug:slug>', create_order, name='create_order'),
]