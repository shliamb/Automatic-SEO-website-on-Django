from django.contrib.sitemaps import Sitemap
from .models import Page

class PageSitemap(Sitemap):
    changefreq = 'weekly'  # Частота изменений
    priority = 0.9         # Приоритетность страниц

    def items(self):
        return Page.objects.filter(publish=True) # Возвращает QuerySet объектов, которые будут отображаться в карте сайта

    def lastmod(self, obj):
        return obj.updated  # Возвращает дату последнего изменения объекта
