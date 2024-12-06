from django.shortcuts import render, HttpResponse
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ShowProduct
from rest_framework.generics import ListCreateAPIView
from django.views.decorators.cache import cache_page


# Create your views here.
def index(request):
	return HttpResponse("Caching")

class products(ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ShowProduct


@cache_page(60*15)
def cached(request):
	all_produts = Product.objects.all()
	serializer = ShowProduct(all_produts, many=True)
	return Response({'products':serializer.data})