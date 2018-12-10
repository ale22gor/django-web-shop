from django.contrib import admin
from .models import OrderSummary
from django.db.models import Count, Sum, F
@admin.register(OrderSummary)
class OrderSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/order_summary_change_list.html'
    date_hierarchy = 'created'
    def changelist_view(self, request, extra_context=None):
        
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        
        queryset = OrderSummary.objects.filter(product__Category='Action')
        ##queryset = OrderSummary.objects.filter()
        print(queryset.values())
        response.context_data['orderItems'] = queryset
        
        return response