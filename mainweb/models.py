from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # Модель встроена

# Модель Страницы
class Page(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок:')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='URL страницы:')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор:') # автора берет из таблицы User встроенной ко связи ключа для нормализации базы
    body = models.TextField(verbose_name='Основной текст стр-цы:')
    seotitle = models.CharField(max_length=250, verbose_name='Title:') # заголовок title страницы в html
    keywords = models.CharField(max_length=250, verbose_name='Keywords:') 
    description = models.TextField(max_length=550,verbose_name='Description:')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Публикация:')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создана:')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлена:')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children',  verbose_name='Родитель:') # Родительские отношения
    views = models.PositiveIntegerField(default=0, verbose_name='Просмотры:') # просмотры страницы

    def __str__(self):
        return self.title

# Модель свободных текстовых блоков на страницах 
class Modul(models.Model): # дополнительные блоки на страницах
    title = models.CharField(max_length=100, verbose_name='Заголовок модуля')
    body = models.TextField(verbose_name='Основной текст модуля') # Основной текст модуля
    publish = models.DateTimeField(default=timezone.now, verbose_name='Время публикации')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    active = models.BooleanField(default=False, verbose_name='Скрыть модуль') # Активный модуль или скрыт

    def __str__(self):
        return self.title

# YouTube
# class YouTube(models.Model):
#     pass

#     def __str__(self):
#         return self.title


# Telegram
# class Telegram(models.Model):
#     pass

#     def __str__(self):
#         return self.title
    
# 1. Кастом модуль
# 2. Картинки 
# 3. Тэги
