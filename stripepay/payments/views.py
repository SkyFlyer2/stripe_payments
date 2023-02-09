from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render, get_object_or_404


class MainPage(TemplateView):
    template_name = 'index.html'


def item_detail(request, id):
    template_name = 'index.html'


def item_purchase(request, id):
    template_name = 'index.html'
