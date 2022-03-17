from rest_framework import serializers
from .models import *

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ["id", "name", "location"]
        
        
class ProductSerializer(serializers.ModelSerializer):
    total_amount = serializers.ReadOnlyField()
    sales_price = serializers.ReadOnlyField()
    
    class Meta:
        model = Product
        fields = ('user', 'warehouse', 'name', 'price', 'quantity', 'sku', 'date', 'total_amount', 'sales_price')
        
       
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        
        
class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'