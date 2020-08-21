from django.contrib import admin
from .models import post, Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ('title','date_posted', 'author')
	search_fields = ('title', 'content')

admin.site.register(post)
admin.site.register(Comment)
