from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from mainweb.sitemaps import PageSitemap

sitemaps = {
    'pages': PageSitemap,
}

urlpatterns = [
    path('administrator/', admin.site.urls),
    path('', include('mainweb.urls')), # перенаправление url верхнего порядка на url нижнего порядка в mainweb/url.py
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'), # карта сайта
]
