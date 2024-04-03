from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import OrderForm, CreateUserForm, CustomerForm
from .decorators import unauthenticated_user, allowed_users, admin_only
# from .filters import OrderFilter


@login_required(login_url='login')
@admin_only
def index(request):
    """ a view to return the index page """
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
        'total_customers': total_customers,
        'delivered': delivered,
        'pending': pending
        }

    return render(request, 'market/index.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'market/products.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):

    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product',
                                         'status'), extra=6)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == "POST":
        form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('index')

    context = {
        'form': formset
    }
    return render(request, 'market/order_form.html', context)


@login_required(login_url='login')
def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    print('ORDER:', order)
    if request.method == 'POST':

        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form':form
        }

    return render(request, 'market/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):

    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('index')
    context = {
        'order': order
    }
    return render(request, 'market/delete.html', context)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user
            )
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'market/register.html', context)


@unauthenticated_user
def loginPage(request):
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):

    orders = request.user.customer.order_set.all()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
        }

    return render(request, 'market/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES,instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated')
        else:
            messages.error(request, 'Profile not updated at this time,\
                please try again or contact us')

    context = {
        'form':form
        }
    return render(request, 'market/account_settings.html', context)
