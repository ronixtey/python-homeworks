from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ["body", "user", "pub_date"]
	list_filter = ["pub_date", "user"]
	search_fields = ["body", "title"]


class CommentAdmin(admin.ModelAdmin):
	list_filter = ["pub_date", "user", "post"]
	search_fields = ["body"]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)