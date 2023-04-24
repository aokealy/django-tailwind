from django.contrib import admin

from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class orderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    inlines = [OrderItemInline]   

admin.site.register(Order, orderAdmin)
admin.site.register(OrderItem)
