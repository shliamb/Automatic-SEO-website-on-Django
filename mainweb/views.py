from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Page


def home(request):
    page = get_object_or_404(Page, slug='home') # Получаем все объекты модели Page
    return render(request, 'mainweb/home.html', {'page': page})


def page_detail(request, slug):
    # Если slug равен 'home', то редирект на главную без 'home'
    if slug == 'home':
        return redirect('home')
    
    # Если slug равен None, генерировать 404 ошибку
    if slug is None:
        raise Http404("Страница не найдена")
    
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'mainweb/pages/page_detail.html', {'page': page})

