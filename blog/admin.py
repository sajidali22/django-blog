from django.contrib import admin
from .models import post, Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ('title','date_posted', 'author')
	search_fields = ('title', 'content')

admin.site.register(post)
admin.site.register(Comment)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'post', 'created_date ', 'approved_comment')
    list_filter = ('active', 'created_date ')
    search_fields = ('author', 'text')
    actions = ['approved_comment']