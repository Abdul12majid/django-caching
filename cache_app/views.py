from django.shortcuts import render, HttpResponse
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ShowProduct
from rest_framework.generics import ListCreateAPIView


# Create your views here.
def index(request):
	return HttpResponse("Caching")

class products(ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ShowProduct