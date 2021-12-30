from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('products', views.products, name='products'),
    path('customer', views.customer, name='contact'),

]