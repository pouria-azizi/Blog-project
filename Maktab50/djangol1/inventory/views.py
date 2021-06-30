from django.views.generic import ListView
from . import models
from rest_framework import generics
from . import serializers


class ListProductView(ListView):
    """
    shows a list of active products
    """
    queryset = models.Product.objects.filter(is_active=True)
    # paginate_by = 6


"""
REST Views
"""


class ProductList(generics.ListAPIView):
    queryset = models.Product.objects.filter(is_active=True)
    serializer_class = serializers.ProductSerializer
