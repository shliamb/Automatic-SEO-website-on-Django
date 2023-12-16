from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')
    list_filter = ('title', 'created_date', 'published_date', 'author')
    search_fields = ('title', 'author')
    #prepopulated_fields = {'author': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'published_date'
    ordering = ['author', 'published_date']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_date', 'approved_comment')
    list_filter = ('post', 'author', 'created_date', 'approved_comment')
    search_fields = ('post', 'author')
    #prepopulated_fields = {'author': ('title',)}
    #raw_id_fields = ('author',)
    date_hierarchy = 'created_date'
    ordering = ['author', 'created_date']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)



