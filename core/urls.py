from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="item-list"),
    path('checkout-page/', views.checkout, name="checkout"),
    path('product-page/', views.products, name="product"),
    path('base/', views.base, name="base"),

]
