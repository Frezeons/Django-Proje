from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Product
@admin.register(Product)
class ProductAdmin(ModelAdmin):  
    list_display = ("name", "category", "quantity", "price", "added_date")
    search_fields = ("name", "category")
# Register your models here.
