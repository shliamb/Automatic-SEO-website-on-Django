from django.contrib import admin
from django.urls import path, include

# перенаправление url верхнего порядка на url нижнего порядка в mainweb/url.py
urlpatterns = [
    path('administrator/', admin.site.urls),
    path('', include('mainweb.urls')),
]