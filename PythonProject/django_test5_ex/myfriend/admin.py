from django.contrib import admin
from myfriend.models import Friends

# Register your models here.
class FriendsAdmin(admin.ModelAdmin):  # ModelAdmin을 상속받는다.
    list_display = ('id', 'name', 'addr', 'age')
    

admin.site.register(Friends, FriendsAdmin)