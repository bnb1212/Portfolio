from django.contrib import admin
from myproduct.models import Producttab

# Register your models here.
class ProductAdmin(admin.ModelAdmin):  # ModelAdmin을 상속받는다.
    list_display = ('id', 'pname', 'category', 'price', 'stock', 'description')
    

admin.site.register(Producttab, ProductAdmin)