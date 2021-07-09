from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import responses

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


@csrf_exempt
def products_list(request):
    if request.method =='GET':
        qs = models.Product.objects.all()
        serializer = serializers.ProductSerializer(qs, many=True)
        return  JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class ProductList2(APIView):
    pass