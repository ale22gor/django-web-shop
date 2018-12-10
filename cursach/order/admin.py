from django.contrib import admin
from .models import OrderSummary,Order, OrderItem, Adress
from django.db.models import Count, Sum, Min, Max
from django.db.models.functions import Trunc
from django.db import models

class AdressItemInline(admin.TabularInline):
    
    model = Adress
class OrderItemInline(admin.TabularInline):
    
    model = OrderItem
    raw_id_fields = ['product']
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
    'paid','created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    list_editable = ['paid']
    inlines = [AdressItemInline, OrderItemInline]

admin.site.register(Order,OrderAdmin)
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
        
        metrics = {
            'total': Sum('quantity'),
            'total_sales': Sum('product__Price'),
        }
        response.context_data['summary'] = list(
            qs
            .values('product__Category')
            .annotate(**metrics)
            .order_by('-total_sales')
        )
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )
        summary_over_time = qs.annotate(
            period=Trunc(
                'created',
                'day',
                output_field=models.DateTimeField(),
            ),
        ).values('period').annotate(total=Sum('product__Price')).order_by('period')
        summary_range = summary_over_time.aggregate(
            low=Min('total'),
            high=Max('total'),
        )
        high = summary_range.get('high', 0)
        low = summary_range.get('low', 0)
        response.context_data['summary_over_time'] = [{
            'period': x['period'],
            'total': x['total'] or 0,
            'pct': \
               ((x['total'] or 0) - low) / (high - low) * 100 
               if high > low else 0,
        } for x in summary_over_time]
        
        list_filter = [ 'created']

        return response