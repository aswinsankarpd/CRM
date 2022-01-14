from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

def dashboard(request):
    order = Order.objects.all()
    customer = Customer.objects.all()
    total_orders = order.count()
    customer_count = customer.count()
    delivered_count = Order.objects.all().filter(status="Delivered").count()

    context = {"order":order,"customer":customer,"total_orders":total_orders,"customer_count":customer_count,"delivered_count":delivered_count}
    return render(request,'mainapp/dashboard.html',context)

def products(request):
    products = Product.objects.all()
    context = {"product":products}
    print(products)
    return render(request,'mainapp/product.html',context)

def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    order_count = customer.order_set.all().count()
    orders = customer.order_set.all()
    context = {"customer":customer,"order_count":order_count,"orders":orders}
    return render(request,'mainapp/customer.html',context)

def create_order(request):
    form = OrderForm()

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/create_order')
    context = {'form':form}
    return render(request,'mainapp/order_form.html',context)