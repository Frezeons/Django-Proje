from django.contrib import admin
from .models import Depo, Product  

@admin.register(Depo)
class DepoAdmin(admin.ModelAdmin):
    list_display = ('ad', 'adres')  
    search_fields = ('ad',)         

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'depo', 'added_on') 
    list_filter = ('depo',)          
    search_fields = ('name', 'depo__ad')  

# Register your models here.
