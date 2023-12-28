from django.contrib import admin
from .models import Page, Modul, MenuItem




class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'keywords', 'seotitle')
    list_filter = ('keywords', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'

class ModulAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'active')

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_main_menu', 'page', 'order', 'parent', 'active')

admin.site.register(Page, PageAdmin)
admin.site.register(Modul, ModulAdmin)
admin.site.register(MenuItem, MenuItemAdmin)

#admin.site.register(Page)
# admin.site.register(Modul)
# admin.site.register(MenuItem)
