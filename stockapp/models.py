from pyexpat import model
from tkinter import CASCADE
import uuid
from django.db import models
from django.conf import settings

# Create your models here.

class Warehouse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Warehouse Name', max_length=255, blank=False, null=False)
    location = models.CharField(verbose_name='Warehouse Location', max_length=255, blank=False, null=False)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Product Name", max_length=255)
    price = models.DecimalField(verbose_name="Unit Price", decimal_places=2, max_digits=9)
    quantity = models.PositiveIntegerField(verbose_name="Product Quantity")
    sku = models.CharField(verbose_name="Stock Keeping Unit", blank=True, null=True, max_length=50)
    date = models.DateField(verbose_name="Product adding date", auto_now=True)
    
    def __str__(self):
        return self.name
    
    @property
    def total_amount(self):
        return self.quantity * self.price
    
    @property
    def sales_price(self):
        persentage = self.price / 100
        profit = persentage * 15
        return self.price + profit
    
    
class Customer(models.Model):
    first_name = models.CharField(verbose_name="Firstname", max_length=50)
    last_name = models.CharField(verbose_name="Lastname", max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
class Shipment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    destination = models.CharField(verbose_name="Product Shipment Distination", max_length=255)
    quantity = models.PositiveIntegerField(verbose_name="Shipped Product Quantity")
    
    def __str__(self):
        return f'Shipment #{self.id}'
    