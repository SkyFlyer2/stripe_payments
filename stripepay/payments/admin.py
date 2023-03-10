from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price',)
    search_fields = ('name',)
    list_filter = ('price',)
    empty_value_display = '-пусто-'
