from django.contrib.sitemaps import Sitemap
from .models import Page

class PageSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        # Предполагается, что у вас есть булево поле `published` в модели `Page`
        return Page.objects.filter(publish=True)

    # Убедитесь, что метод lastmod возвращает дату/время
    def lastmod(self, obj):
        # здесь должно быть поле, содержащее дату последнего изменения obj, например:
        return obj.updated
    