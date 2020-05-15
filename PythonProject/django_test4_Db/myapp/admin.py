from django.contrib import admin
from myapp.models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):  # ModelAdmin을 상속받는다.
    list_display = ('id', 'code', 'sang', 'price', 'pub_date')
    

admin.site.register(Article, ArticleAdmin)
