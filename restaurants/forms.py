from django import forms
from .models import Restaurants

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurants
        fields = ['name', 'description']


from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'image']
