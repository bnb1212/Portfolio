from django.contrib import admin
from myvote.models import Choice, Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date')
    
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'choice_text', 'votes')
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)