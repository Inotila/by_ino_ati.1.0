from django.urls import path
from . import views

urlpatterns = [
    path('', views.art_display, name='art'),
    path('title/', views.art_detail, name='details')
]
