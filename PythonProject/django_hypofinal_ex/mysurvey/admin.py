from django.contrib import admin
from mysurvey.models import Surveydata

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):  # ModelAdmin을 상속받는다.
    list_display = ('id', 'job', 'gender', 'game_time')
    

admin.site.register(Surveydata, ArticleAdmin)