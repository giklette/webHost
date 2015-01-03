from django.contrib import admin

# Register your models here.



### CHOICE

from polls.models import Choice

#class ChoiceInline(admin.StackedInline):	# version detail
class ChoiceInline(admin.TabularInline):		# version simple
	model = Choice
	extra = 3

#admin.site.register(Choice)




### QUESTION

from polls.models import Question

''' # version NONE
admin.site.register(Question)
'''


''' # version 1
class QuestionAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
'''


'''# version 2
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields': ['question_text']}),
		('Date information',	{'fields': ['pub_date']}),
	]

admin.site.register(Question, QuestionAdmin)
'''

''' # version 3
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields': ['question_text']}),
		('Date information',	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]

admin.site.register(Question, QuestionAdmin)
'''

''' # version 4
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields': ['question_text']}),
		('Date information',	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]		# cf. class ChoiceInline(admin.StackedInline)

admin.site.register(Question, QuestionAdmin)
'''

# version 5
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields': ['question_text']}),
		('Date information',	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]		# cf. class ChoiceInline(admin.StackedInline)
	#list_display = ('question_text', 'pub_date')
	list_display = ('question_text', 'pub_date', 'was_published_recently')

#admin.site.register(Question, QuestionAdmin)
#admin.site.register(Question, QuestionAdmin, list_filter = ['pub_date'])
admin.site.register(Question, QuestionAdmin, list_filter = ['pub_date'], search_fields = ['question_text'])


