from django.contrib import admin

# Register your models here.
from .models import Choice, Question

#wow that admin.StackedInline/TabularInline is AWESOME!
class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

# for custimization:
class QuestionAdmin(admin.ModelAdmin):
  #setting these variables sets the options for class
  fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 
          'classes': ['collapse']}),
    ]
  inlines = [ChoiceInline]
  list_display = ('question_text', 'pub_date', 'was_published_recently')
  list_filter = ['pub_date']
  search_fields = ['question_text']
# pass in the model admin class as a second argument 

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)