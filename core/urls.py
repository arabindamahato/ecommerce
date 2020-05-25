from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="item-list"),
    path('checkout/', views.checkout, name="checkout"),
    path('product/<slug>/', views.ItemDetailView.as_view(), name="product"),
    path('base/', views.base, name="base"),
    path('add-to-cart/<slug>/', views.add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<slug>/',
         views.remove_from_cart, name="remove-from-cart"),

]
