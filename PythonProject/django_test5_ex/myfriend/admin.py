from django.contrib import admin
from myfriend.models import Friends

# Register your models here.
class FriendsAdmin(admin.ModelAdmin):  # ModelAdmin�� ��ӹ޴´�.
    list_display = ('id', 'name', 'addr', 'age')
    

admin.site.register(Friends, FriendsAdmin)