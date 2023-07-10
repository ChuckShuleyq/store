from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('products.html', views.products, name="products")
]