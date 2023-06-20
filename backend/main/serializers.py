from rest_framework import serializers
from .models import Vendor, Category, Product

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'