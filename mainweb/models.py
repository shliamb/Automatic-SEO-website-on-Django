from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Модиль Страницы
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

    def __str__(self):
        return self.title

# Модель меню
class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    is_main_menu = models.BooleanField(default=True)  # Является ли элемент главным меню
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')  # Ссылка на родительский элемент
    page = models.OneToOneField(Page, on_delete=models.CASCADE, null=True, blank=True) # Указывает на связь с моделью Page может быть null и может быть пустым, один пунктт меню к одномой странице
    url = models.CharField(max_length=200) # Можно внешнию ссылку
    active = models.BooleanField(default=False) # Активное меню для визуализации
    order = models.PositiveIntegerField(default=0) # порядок отображения от 0 - 5 к примеру

    def __str__(self):
        return self.title

# Модель блоков  
class Modul(models.Model): # дополнительные блоки на страницах
    title = models.CharField(max_length=100)
    body = models.TextField() # Основной текст модуля
    author = models.ForeignKey(User, on_delete=models.CASCADE) # автора берет из таблицы User встроенной ко связи ключа для нормализации базы
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title