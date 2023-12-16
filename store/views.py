from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import JsonResponse
import json
from django.contrib.auth.forms import UserCreationForm
from .utils import *
from .form import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('store')
    
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    context = {'cartItems' : cartItems}
    return render(request, 'accounts/login.html', context)

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created')
            Customer.objects.create(
                user=user,
                name=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email')
            )
            return redirect('login')
    
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    context = {'form' : form, 'cartItems' : cartItems}
    return render(request, 'accounts/register.html', context)

def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    # products = Products.objects.filter(quantity__gt=0)
    products = Products.objects.all()
    context = {'products': products, 'cartItems': cartItems, 'cartlength': 0}
    return render(request, 'store.html', context)


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'cart.html', context)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    print(f'checkout: {cartItems}')
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'checkout.html', context)


def product_details(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    context = {'product': product}
    return render(request, 'detail.html', context)
# Create your views here.


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Products.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    print('item was added')
    return JsonResponse('Item was added', safe=False)
