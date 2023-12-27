from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Страница
class Page(models.Model):
    title = models.CharField(max_length=250) # Заголовок статьи на странице, если нужна будет ссылка с названием
    description = models.TextField()
    keywords = models.CharField(max_length=250) 
    seotitle = models.CharField(max_length=250) # заголовок title страницы в html
    slug = models.SlugField(max_length=250, unique=True) # url страницы
    author = models.ForeignKey(User, on_delete=models.CASCADE) # автора берет из таблицы User встроенной ко связи ключа для нормализации базы
    body = models.TextField() # Основной текст
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Page(models.Model):
    title = models.CharField(max_length=250)


def __str__(self):
    return self.title