from django.shortcuts import render
from django.http import HttpResponse


def dashboard(request):
    return render(request,'mainapp/dashboard.html')

def products(request):
    return render(request,'mainapp/product.html')

def customer(request):
    return render(request,'mainapp/customer.html')