from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('products', views.products, name='products'),
    path('customer_profile/<str:pk_test>', views.customer, name='customer'),

]