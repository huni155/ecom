from django.contrib import admin
from .models import *



class OrderitemsInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'complete', 'date_ordered']
    readonly_fields = ['customer', 'date_ordered']
    list_filter = ['complete', 'date_ordered', 'customer']
    inlines = [OrderitemsInline]

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['name__startswith']

admin.site.register(Products)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Customer, CustomerAdmin)