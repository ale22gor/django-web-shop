from django.contrib import admin
from django.db.models import Count, Sum, Min, Max, Avg
from django.db.models.functions import Trunc
from .models import CommentSummary
# Register your models here.
@admin.register(CommentSummary)

class CommentSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/comment_summary_change_list.html'
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
            'count': Count('id'),
            'total': Avg('rating'),
        }
        response.context_data['summary'] = list(
            qs
            .values('product__Name')
            .annotate(**metrics)
            .order_by('-total')
        )
        return response