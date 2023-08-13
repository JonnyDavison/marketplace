from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import orderForm

def index(request):
    """ a view to retuern the index page """
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
    }

    return render(request, 'market/index.html', context)


def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    order_count = orders.count()

    context = {
        'customer': customer,
        'orders': orders,
        'order_count': order_count
        }
    return render(request, 'market/customer.html', context)


def products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'market/products.html', context)


def createOrder(request):
    form = orderForm()
    if request.method == "POST":
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'market/order_form.html', context)


def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = orderForm(instance=order)

    if request.method == "POST":
        form = orderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'market/order_form.html', context)


def deleteOrder(request, pk):

    order = Order.objects.get(id=pk)
    context = {
        'order': order
    }
    return render(request, 'market/delete.html', context)