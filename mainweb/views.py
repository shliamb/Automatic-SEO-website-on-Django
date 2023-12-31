from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Page

# Главная страница = home
def home(request):
    page = get_object_or_404(Page, slug='home') # Получаем все объекты модели Page где slug = home
    root_pages = Page.objects.filter(parent=None)  # Получаем все корневые страницы
    context = {
        'page': page,
        'root_pages': root_pages
    }
    return render(request, 'mainweb/home.html', context)


# Обработка родительской страницы 1го уровня: <slug:slug>/
def page_detail(request, slug):
    if slug == 'home':
        return redirect('home')

    page = get_object_or_404(Page, slug=slug)

    if page.parent is not None:
        raise Http404("Страница не найдена")     

    root_pages = Page.objects.filter(parent=None)  # Получаем все корневые страницы

    context = {
        'page': page,
        'root_pages': root_pages
    }
    return render(request, 'mainweb/pages/page_detail.html', context)

def my_view(request):
    root_pages = Page.objects.filter(parent=None)  # Получаем все корневые страницы
    return render(request, 'my_template.html', {'root_pages': root_pages})


# Обработка дочерней страницы 2го уровня: <slug:parent_slug>/<slug:slug>/
def sub_page_detail(request, parent_slug, slug):
    parent_page = get_object_or_404(Page, slug=parent_slug)
    page = get_object_or_404(Page, slug=slug, parent=parent_page)
    root_pages = Page.objects.filter(parent=None)  # Получаем все корневые страницы
    context = {
        'page': page,
        'root_pages': root_pages
    }
    return render(request, 'mainweb/pages/page_detail.html', context)