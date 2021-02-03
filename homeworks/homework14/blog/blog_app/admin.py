from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class CommentInline(admin.TabularInline):
	model = Comment
	fields = ['user', 'body', 'pub_date']
#	extra = 1	by default = 3

class PostAdmin(admin.ModelAdmin):
	list_display = ["title", "user", "pub_date"]
	list_filter = ["pub_date", "user"]
	search_fields = ["body", "title"]
	fields = ['title', 'body', 'user', 'pub_date']

	inlines = [CommentInline]

# class CommentAdmin(admin.ModelAdmin):
# 	list_filter = ["pub_date", "user", "post"]
# 	search_fields = ["body"]


admin.site.register(Post, PostAdmin)
# admin.site.register(Comment, CommentAdmin)