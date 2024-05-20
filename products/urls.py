from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('', views.home_page, name='index'),
    path('products/<slug:slug>/', views.detail_page, name='detail'),
]