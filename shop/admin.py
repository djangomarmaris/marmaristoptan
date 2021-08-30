from django.contrib import admin
from django import forms
from .models import Category,Product
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','parent','name','slug']
    prepopulated_fields = {'slug':('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','category','price','available','created','updated']
    list_filter = ['available','created','updated','category']
    list_editable = ['price','available']
    prepopulated_fields = {'slug':('name',)}

class ModelClass:
    ## content = models.TextField()bu ile modeldeki classı belirleriz burayada dikkat.
    description = RichTextUploadingField()

class PostForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())



admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.site_header = '@Enjoy.com / Developer @ İhsan Gürol Demirtaş'



