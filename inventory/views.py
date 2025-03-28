from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegistry, ProductForm, OrderForm, InquiryForm, SupplierForm, EquipmentForm, PriceForm
from .models import Product, Order, Equipment, Supplier, Price
from django.db.models import F
from django.http import HttpResponseRedirect


@login_required
def index(request):
    orders_user = Order.objects.all()
    users = User.objects.all()[:2]
    orders_adm = Order.objects.all()[:2]
    products = Product.objects.all()[:2]
    reg_users = len(User.objects.all())
    all_prods = len(Product.objects.all())
    all_orders = len(Order.objects.all())
    context = {
        "title": "Home",
        "orders": orders_user,
        "orders_adm": orders_adm,
        "users": users,
        "products": products,
        "count_users": reg_users,
        "count_products": all_prods,
        "count_orders": all_orders,
    }
    return render(request, "inventory/index.html", context)

@login_required
def products(request):
    products = Product.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm()
    context = {"title": "Products", "products": products, "form": form}
    return render(request, "inventory/products.html", context)

@login_required
def orders(request):
    orders = Order.objects.all()
    print([i for i in request])
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            instance.save()
            return redirect("orders")
    else:
        form = OrderForm()
    context = {"title": "Orders", "orders": orders, "form": form}
    return render(request, "inventory/orders.html", context)

@login_required
def users(request):
    users = User.objects.all()
    context = {"title": "Users", "users": users}
    return render(request, "inventory/users.html", context)

@login_required
def user(request):
    context = {"profile": "User Profile"}
    return render(request, "inventory/user.html", context)

def register(request):
    if request.method == "POST":
        form = UserRegistry(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistry()
    context = {"register": "Register", "form": form}
    return render(request, "inventory/register.html", context)

def price_comparison(request, equipment_id):
    equipment = Equipment.objects.get(id=equipment_id)
    prices = equipment.prices.all()
    lowest_price = prices.order_by('price').first()
    return render(request, 'inventory/price_comparison.html', {'equipment': equipment, 'prices': prices, 'lowest_price': lowest_price})

def send_inquiry(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            equipment = form.cleaned_data['equipment']
            message = form.cleaned_data['message']
            contact_email = form.cleaned_data['contact_email']

            # Send the email
            # send_mail(
            #     f"Inquiry for {equipment.name}",
            #     f"Message: {message}\n\nContact Email: {contact_email}",
            #     settings.DEFAULT_FROM_EMAIL,
            #     ['supplier@example.com'],  # Supplier email, you can dynamically fetch based on equipment
            # )

            return HttpResponseRedirect('/thank-you/')  # Redirect after sending the email
    else:
        form = InquiryForm()

    return render(request, 'inventory/inquiry_form.html', {'form': form})

@login_required
def suppliers(request):
    suppliers = Supplier.objects.all()
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("suppliers")
    else:
        form = SupplierForm()
    context = {"title": "Suppliers", "suppliers": suppliers, "form": form}
    return render(request, "inventory/supplier.html", context)

@login_required
def equipments(request):
    equipments = Equipment.objects.all()
    if request.method == "POST":
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("equipments")
    else:
        form = EquipmentForm()
    context = {"title": "Equipments", "equipments": equipments, "form": form}
    return render(request, "inventory/equipment.html", context)

@login_required
def add_prices(request):
    prices = Price.objects.all()
    if request.method == 'POST':
        form = PriceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_prices')
    else:
        form = PriceForm()
    context = {"title": "add_price", "prices": prices, "form": form}
    return render(request, 'inventory/add_prices.html', context)