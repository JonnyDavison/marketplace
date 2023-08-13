from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages


def index(request):
    """ a view to retuern the index page """

    return render(request, 'market/index.html')


def customer(request):

    return render(request, 'market/customer.html')


def products(request):

    return render(request, 'market/products.html')
