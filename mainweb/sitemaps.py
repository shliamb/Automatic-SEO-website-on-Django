from django.contrib.sitemaps import Sitemap
from .models import Page


class PageSitemap(Sitemap):
    changefreq = 'weekly'

    def items(self):
        return Page.objects.filter( # Возвращаем только те страницы, которые опубликованы, либо не имеют родителя, либо имеют опубликованного родителя
            publish=True,
            parent__publish=True
        ) | Page.objects.filter(  # знак | означает логический оператор или
            publish=True,
            parent__isnull=True
        )
    def priority(self, obj):
        if obj.parent is None: # Если у страницы нет родителя, то это главная страница. Даем ей высокий приоритет.
            return 0.9
        return 0.5 # Если же родитель есть - это дочерняя страница. Даем ей меньший приоритет.

    def lastmod(self, obj):
        return obj.updated
