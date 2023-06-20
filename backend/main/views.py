from django.shortcuts import render
from rest_framework import generics
from .serializers import Vendor, VendorSerializer

# Create your views here.
class VendorList(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer