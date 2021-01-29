from django.contrib import admin
from .models import UserQuestion, Answer, UserLikes, UserDislikes

# Register your models here.
admin.site.register(UserQuestion)
admin.site.register(Answer)
admin.site.register(UserLikes)
admin.site.register(UserDislikes)