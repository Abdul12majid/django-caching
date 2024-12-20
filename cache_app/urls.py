from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('products/', views.products.as_view()),
    path('cached/', views.cached, name="cached"),
]