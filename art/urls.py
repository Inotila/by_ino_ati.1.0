from django.urls import path
from . import views

urlpatterns = [
    path('', views.art_display, name='art'),
    path('title/<int:id>/', views.art_detail, name='details'),
    path('like/<int:id>/', views.like_item, name='like_art_piece'),
]
