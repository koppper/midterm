from django.urls import path
from .views import product_list, add_restaurant, restaurant_list, restaurant_detail, add_product, about, delete_product, delete_restaurant
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('', product_list, name='product_list'),
    path('about/', about, name='about'),
    path('add-restaurant/', add_restaurant, name='add_restaurant'),
    path('restaurants/', restaurant_list, name='restaurant_list'),
    path('restaurants/<int:id>/', restaurant_detail, name='restaurant_detail'),
    path('restaurant/<int:restaurant_id>/add_product/', login_required(add_product), name='add_product'),
    path('product_delete/<int:pk>/', delete_product, name='delete_product'),
    path('delete_restaurant/<int:pk>/', delete_restaurant, name='delete_restaurant')

]
