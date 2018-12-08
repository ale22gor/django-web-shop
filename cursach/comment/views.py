from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Comment



@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    product_pk=comment.product.pk
    comment.approve()
    return redirect('product:detail', pk=product_pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    product_pk=comment.product.pk
    comment.delete()
    return redirect('product:detail', pk=product_pk)