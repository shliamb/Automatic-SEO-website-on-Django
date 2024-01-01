from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('<slug:slug>/', views.page_detail, name='page_detail'),  # Страницы первого уровня
    path('<slug:parent_slug>/<slug:slug>/', views.sub_page_detail, name='sub_page_detail'),  # Страницы второго уровня
]
