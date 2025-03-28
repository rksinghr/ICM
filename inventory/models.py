from email.policy import default
from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ("Stationary", "Stationary"),
    ("Electronics", "Electronics"),
    ("Food", "Food"),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    physical_address = models.CharField(max_length=40, null=True)
    mobile = models.CharField(max_length=12, null=True)
    picture = models.ImageField(default="avatar.jpeg", upload_to="Pictures")

    def __str__(self) -> str:
        return self.user.username

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.product} ordered quantity {self.order_quantity}"

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Price(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='prices')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    effective_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.equipment.name} from {self.supplier.name} - ${self.price}"
