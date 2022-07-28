from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<int:art_id>/', views.add_art_to_bag, name='add_art_to_bag'),
]
