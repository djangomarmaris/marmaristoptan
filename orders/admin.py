from django.contrib import admin
from .models import Order, OrderItem ,ReturnData ,WebhookData ,UserTokenData


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



class ReturnDataAdmin(admin.ModelAdmin):
    list_display = ['status']


class WebHookAdmin(admin.ModelAdmin):
    list_display = ['status']


class UserDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'usertoken']


admin.site.register(Order, OrderAdmin)
admin.site.register(ReturnData,ReturnDataAdmin)
admin.site.register(WebhookData,WebHookAdmin)
admin.site.register(UserTokenData, UserDataAdmin)

