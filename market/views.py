from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import *


def index(request):
    """ a view to retuern the index page """
    orders = Order.objects.all()
    customers = Customer.objects.all()

    context = {
        'orders': orders,
        'customers': customers
    }

    return render(request, 'market/index.html', context)


def customer(request):

    return render(request, 'market/customer.html')


def products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'market/products.html', context)
