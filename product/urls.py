from django.urls import path 
from . import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('page/<int:page_number>/', views.products, name="paginator"),
    path('products/category/<category_id>/', views.products, name="category"),
    path('baskets/add/<int:product_id>/', views.basket_add, name="basket_add"),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name="basket_remove")
]
app_name = 'product'