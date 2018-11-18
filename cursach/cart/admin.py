from django.contrib import admin
from django.utils.datetime_safe import datetime

from cart.models import  Cart, Entry


class EntryAdmin(admin.ModelAdmin):
    # Overide of the save model
    def save_model(self, request, obj, form, change):
        obj.cart.total += obj.quantity * obj.product.Price
        obj.cart.count += obj.quantity
        ##obj.cart.updated = datetime.now()
        obj.save()
        super().save_model(request, obj, form, change)

# Register your models here.
admin.site.register(Cart)
admin.site.register(Entry, EntryAdmin)