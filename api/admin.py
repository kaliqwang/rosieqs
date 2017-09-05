from django.contrib import admin

from .models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'initial_quantity', 'quantity')

class EventAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity_change', 'timestamp')

admin.site.register(Item, ItemAdmin)
admin.site.register(Event, EventAdmin)
