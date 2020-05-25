from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView
from core.models import Item, OrderItem, Order


def checkout(request):
    return render(request, "checkout.html")


def base(request):
    return render(request, "base.html")


class HomeView(ListView):
    model = Item
    template_name = "home.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)  # to get the item
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "The item quantity was updated.")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("core:product", slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        # here "core:product" = product is url name core is appname with slug
        return redirect("core:product", slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)  # to get the item
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]  # get the order
        # check the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():

            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
        else:
            messages.info(request, "This item is not in your cart.")
            return redirect("core:product", slug=slug)

    else:
        messages.info(request, "you don't have an active order.")
        return redirect("core:product", slug=slug)
    return redirect("core:product", slug=slug)
