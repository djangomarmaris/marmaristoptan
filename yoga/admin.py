from django.contrib import admin
from .models import kvvk
# Register your models here.




class KVKKAdmin(admin.ModelAdmin):
    list_display = ['name']







admin.site.register(kvvk,KVKKAdmin)