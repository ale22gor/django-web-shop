from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['Name','Amount', 'Price', 'PurchaisePrice',
    'Category']
    list_filter = ['Category']
    list_editable = ['Price', 'Amount']
admin.site.register(Product, ProductAdmin)