from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('products', views.products, name='products'),
    path('customer_profile/<str:pk_test>', views.customer, name='customer'),
    path('create_order', views.create_order, name='create_order'),
    path('update_order/<str:pk_test>', views.update_order, name='update_order'),
    path('remove_order/<str:pk_test>', views.remove_order, name='remove_order')
]