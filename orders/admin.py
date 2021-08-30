from django.contrib import admin
from .models import Order, OrderItem


class Back_Admin(admin.ModelAdmin):
    list_display = ["author", "order_no", "cargo","created_date","case"]

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

# 'paid', 'tokenCheck',

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'city', 'created','updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)

