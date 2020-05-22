from django.contrib import admin
from core.models import Order, Item, OrderItem

admin.site.register(Order)
admin.site.register(Item)
admin.site.register(OrderItem)
