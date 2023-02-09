from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render, get_object_or_404

from .models import Item


class MainPage(TemplateView):
    template_name = 'index.html'


def item_detail(request, id):
    item = get_object_or_404(Item, pk= id)
    return render(
        request,
        'item_detail.html',
        {'buy_item': item,}
    )


def item_purchase(request, id):
    template_name = 'index.html'
