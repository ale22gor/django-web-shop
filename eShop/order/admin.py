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
    list_filter = (
                    'paid', 
                   'created',
                   'updated',
                  )
    list_editable = ['paid']
    inlines = [AdressItemInline, OrderItemInline]

admin.site.register(Order,OrderAdmin)

def get_next_in_date_hierarchy(request, date_hierarchy):
    if date_hierarchy + '__day' in request.GET:
        return 'hour'
    if date_hierarchy + '__month' in request.GET:
        return 'day'
    if date_hierarchy + '__year' in request.GET:
        return 'week'
    return 'month'

@admin.register(OrderSummary)


class OrderSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/order_summary_change_list.html'
    date_hierarchy = 'created'
    search_fields = ['order__user__username', 'product__Name']
    list_filter = (
            ('product__Category'),
            'created',
        )
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        SalesQs = Sum('product__Price')
        ExpenseQs = Sum('product__PurchaisePrice')
        SurplusQs = SalesQs - ExpenseQs
        metrics = {
            'total': Sum('quantity'),
            'total_sales': SalesQs,
            'expenses': ExpenseQs,
            'surplus': SurplusQs,
        }
        response.context_data['summary'] = list(
            qs
            .values('product__Category')
            .annotate(**metrics)
            .order_by('-expenses')
        )
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )
        
        period = get_next_in_date_hierarchy(
            request,
            self.date_hierarchy,
        )
        response.context_data['period'] = period
        
        
        summary_over_time = qs.annotate(
            period=Trunc('created', period, output_field=models.DateTimeField(),),
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
        
        
        return response