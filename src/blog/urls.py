from django.urls import path 
from . import views

urlpatterns = [
    path('blog/', views.post_list, name='post_list'),
    path('blog/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/post/new/', views.post_new, name='post_new'),
    path('blog/post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #path('get-paginated-posts/', views.get_paginated_posts, name='get_paginated_posts'),  # Добавленный URL-путь
    path('', views.home, name='home'),
]