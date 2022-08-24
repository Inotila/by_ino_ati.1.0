from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_done<order_number>', views.checkout_done, name='checkout_done'),
]
