from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Page

# Главная страница = home
def home(request):
    page = get_object_or_404(Page, slug='home') # Получаем все объекты модели Page где slug = home
    root_pages = Page.objects.filter(parent=None)  # Получаем все корневые страницы
    page.views += 1 # Увеличение просмотра страницы
    page.save()
    context = {
        'page': page,
        'root_pages': root_pages
    }
    return render(request, 'mainweb/home.html', context)

# Обработка родительской страницы 1го уровня: <slug:slug>/
def page_detail(request, slug):
    if slug == 'home':
        return redirect('home') # Возвращаем /home в /
    page = get_object_or_404(Page, slug=slug) # Получаем страницу согласно совпадению slug
    root_pages = Page.objects.filter(parent=None)  # Получаем все корневые страницы
    if page.parent is not None: # если значение parent не пустое, значит страница дочерняя
        raise Http404("Страница не найдена") # 404 при открытии дочернюю страницу в родительской 
    page.views += 1 # Увеличение просмотра страницы
    page.save()
    context = {
        'page': page,
        'root_pages': root_pages
    }
    return render(request, 'mainweb/pages/page_detail.html', context)

# Обработка дочерней страницы 2го уровня: <slug:parent_slug>/<slug:slug>/
def sub_page_detail(request, parent_slug, slug):
    parent_page = get_object_or_404(Page, slug=parent_slug)
    page = get_object_or_404(Page, slug=slug, parent=parent_page)
    root_pages = Page.objects.filter(parent=None)  # Получаем все корневые страницы
    page.views += 1 # Увеличение просмотра страницы
    page.save()
    context = {
        'page': page,
        'root_pages': root_pages
    }
    return render(request, 'mainweb/pages/page_detail.html', context)

# def get_root_pages():
#     """Возвращает все корневые страницы."""
#     return Page.objects.filter(parent=None)

# def common_page_context(page_slug, parent_slug=None):
#     """Общий контекст для страниц."""
#     if parent_slug:
#         parent_page = get_object_or_404(Page, slug=parent_slug)
#         page = get_object_or_404(Page, slug=page_slug, parent=parent_page)
#     else:
#         page = get_object_or_404(Page, slug=page_slug)

#     return {
#         'page': page,
#         'root_pages': get_root_pages()
#     }

# def home(request):
#     context = common_page_context('home')
#     return render(request, 'mainweb/home.html', context)

# def page_detail(request, slug):
#     if slug == 'home':
#         return redirect('home')
#     context = common_page_context(slug)
#     if context['page'].parent is not None:
#         raise Http404("Страница не найдена")
#     return render(request, 'mainweb/pages/page_detail.html', context)

# def sub_page_detail(request, parent_slug, slug):
#     context = common_page_context(slug, parent_slug)
#     return render(request, 'mainweb/pages/page_detail.html', context)