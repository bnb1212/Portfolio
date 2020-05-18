from django.contrib import admin
from myguest.models import Guest

# Register your models here.
class GuestsAdmin(admin.ModelAdmin):  # ModelAdmin�� ��ӹ޴´�.
    list_display = ('id', 'title', 'content', 'regdate')
    

admin.site.register(Guest, GuestsAdmin)