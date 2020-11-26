from django.contrib import admin
<<<<<<< HEAD
from NewsSection.models import News, Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'date_posted', 'category')
    list_filter = ['author',  'date_posted', 'category']


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_posted')
    list_filter = ('name', 'date_posted')


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentsAdmin)
=======

from NewsSection.models import News

admin.site.register(News)
>>>>>>> 10c795f36d23a00f8ab4fec4346b45eac822fd47
