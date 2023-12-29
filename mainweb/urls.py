from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'), # Главная страница
    path('<slug:slug>/', views.page_detail, name='page_detail'), # Второстепенные страницы
]
