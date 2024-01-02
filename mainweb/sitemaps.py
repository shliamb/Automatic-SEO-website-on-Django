from django.contrib.sitemaps import Sitemap
from .models import Page


class PageSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        # Возвращаем только те страницы, которые опубликованы и
        # либо не имеют родителя, либо имеют опубликованного родителя
        return Page.objects.filter(
            publish=True,
            parent__publish=True
        ) | Page.objects.filter(  # знак | означает логический оператор или
            publish=True,
            parent__isnull=True
        )

    def lastmod(self, obj):
        return obj.updated
