from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import orderForm, CreateUserForm


@login_required(login_url='login')
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
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
        }

    return render(request, 'market/index.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'market/products.html', context)


@login_required(login_url='login')
def createOrder(request, pk):
    
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=6)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == "POST":
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('index')

    context = {
        'formset': formset
    }
    return render(request, 'market/order_form.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def deleteOrder(request, pk):

    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('index')
    context = {
        'order': order
    }
    return render(request, 'market/delete.html', context)


def registerPage(request):

    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
    return render(request, 'market/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'market/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
