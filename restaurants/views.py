from django.shortcuts import render
from .models import Restaurants, Products
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RestaurantForm
from django.contrib import messages
from .forms import ProductForm


def product_list(request):
    restaurant_filter = request.GET.get('restaurant', None)
    products = Products.objects.all()
    if restaurant_filter:
        products = products.filter(restaurant__name=restaurant_filter)
    restaurants = Restaurants.objects.all()
    context = {'products': products, 'restaurants': restaurants, 'restaurant_filter': restaurant_filter}
    return render(request, 'product_list.html', context)

def add_restaurant(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.user = request.user
            restaurant.save()
            return redirect('restaurant_list')

    else:
        form = RestaurantForm()
    return render(request, 'add_restaurant.html', {'form': form})



def restaurant_list(request):
    restaurants = Restaurants.objects.all()
    return render(request, 'restaurant_list.html', {'restaurants': restaurants})


def restaurant_detail(request, id):
    restaurant = get_object_or_404(Restaurants, id=id)
    context = {'restaurant': restaurant}
    return render(request, 'restaurant_detail.html', context)


def add_product(request, restaurant_id):
    restaurant = Restaurants.objects.get(id=restaurant_id)
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.restaurant = restaurant
            product.save()
            messages.success(request, 'Product added successfully')
            return redirect('restaurant_detail', id=restaurant.id)
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form, 'restaurant': restaurant})


def about(request):
    products = Products.objects.all()
    return render(request, "about.html", {"products": products})


def delete_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})


def delete_restaurant(request, pk):
    restaurant = get_object_or_404(Restaurants, pk=pk)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('restaurant_list')
    return render(request, 'delete_restaurant.html', {'restaurant': restaurant})
