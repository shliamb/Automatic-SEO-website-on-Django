from django.contrib import admin
from .models import Page, Modul




class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'keywords', 'seotitle', 'parent')
    list_filter = ('keywords', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    #date_hierarchy = 'publish'

class ModulAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'active')

admin.site.register(Page, PageAdmin)
admin.site.register(Modul, ModulAdmin)

# Простой вывод без классов
#admin.site.register(Page)
# admin.site.register(Modul)
