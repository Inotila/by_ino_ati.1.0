from django.urls import path
from art.views import edit_comment, delete_comment
from . import views

urlpatterns = [
    path('', views.art_display, name='art'),
    path('title/<int:id>/', views.art_detail, name='details'),
    path('like/<int:id>/', views.like_item, name='like_art_piece'),
    path('delete/<comment_id>', delete_comment, name='delete'),
    path('edit/<comment_id>', edit_comment, name='edit'),
]
