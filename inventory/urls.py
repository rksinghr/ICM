# inventory/urls.py
from django.urls import path
from inventory import views

urlpatterns = [
    path("dash/", views.index, name="dash"),
    path("products/", views.products, name="products"),
    path("suppliers/", views.suppliers, name="suppliers"),
    path("equipments/", views.equipments, name="equipments"),
    path("orders/", views.orders, name="orders"),
    path("users/", views.users, name="users"),
    path("user/", views.user, name="user"),
    path("register/", views.register, name="register"),
    path('equipment/<int:equipment_id>/comparison/', views.price_comparison, name='price_comparison'),
    path('inquiry/', views.send_inquiry, name='send_inquiry'),
    path('add-prices/', views.add_prices, name='add_prices'),
]
