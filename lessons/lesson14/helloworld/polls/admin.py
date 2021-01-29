from django.contrib import admin
from .models import Question, Choice, UserChoice

# Register your models here.

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3		# сколько штук


class QuestionAdmin(admin.ModelAdmin):
#	fields = ["pub_date", "body"]
	fieldsets = [	# каждое () - группа полей; (<заголовок>, <поля>)
		(None, {"fields": ["body"]}),					
		("Date info", {"fields": ["pub_date"]})
	]

	inlines = [ChoiceInline]

	# список полей для отображения в списке вопросов 
	list_display = ("body", "pub_date", "was_published_recently")
	# фильтр
	list_filter = ["pub_date", "body"]
	# поиск по полю
	search_fields = ["body"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(UserChoice)
#admin.site.register(Choice)