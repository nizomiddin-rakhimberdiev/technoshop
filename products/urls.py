from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
    path('', views.home_page, name='index'),
    path('products/<slug:slug>/', views.detail_page, name='detail'),
    path('products/<slug:slug>/reviews/<int:id>/', views.delete_review, name='delete_review'),
    path('products/<slug:slug>/edit_review/<int:id>/', views.edit_review, name='edit_review'),
]