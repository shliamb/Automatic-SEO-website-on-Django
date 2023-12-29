from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('administrator/', admin.site.urls), # можно переименовать админку, для сложности ее определения со стороны
    # перенаправление url верхнего порядка на url нижнего порядка
    path('', include('mainweb.urls')),
    path('<slug:slug>/', include('mainweb.urls')),
]

