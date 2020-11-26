from django.contrib import admin
from NewsSection.models import News, Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'date_posted', 'category')
    list_filter = ['author',  'date_posted', 'category']


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_posted')
    list_filter = ('name', 'date_posted')


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentsAdmin)
