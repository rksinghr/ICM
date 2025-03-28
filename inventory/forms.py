from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Order, Equipment, Supplier, Price

class UserRegistry(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password1","password2",]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "quantity", "description"]

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["product", "order_quantity"]

class InquiryForm(forms.Form):
    equipment = forms.ModelChoiceField(queryset=Equipment.objects.all(), widget=forms.Select)
    message = forms.CharField(widget=forms.Textarea)
    contact_email = forms.EmailField()

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ["name", "contact_email"]

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ["name", "description"]

class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ['equipment', 'supplier', 'price', 'effective_date']