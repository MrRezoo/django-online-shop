from django.contrib import admin

# Register your models here.
from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created', 'status')
    list_filter = ('status',)
    inlines = (OrderItemInline,)
