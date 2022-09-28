from django.contrib import admin
from django import forms
from .resources import ProductResource ,CategoryResource
from .models import Category,Product ,Slider
from import_export.admin import ImportExportModelAdmin
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug':('name',)}


    resource_class = CategoryResource


class ProductAdmin(ImportExportModelAdmin):
    list_display = ['name','id','slug','image','category','price','available','index']
    list_filter = ['available','created','updated','category']
    list_editable = ['price','available','index']
    prepopulated_fields = {'slug':('name',)}
    exclude = ('id',)

    resource_class = ProductResource

class ModelClass:
    ## content = models.TextField()bu ile modeldeki classı belirleriz burayada dikkat.
    description = RichTextUploadingField()

class PostForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())



class SliderAdmin(admin.ModelAdmin):
    list_display = ['h1']

admin.site.register(Slider,SliderAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.site_header = '@Enjoy.com / Developer @ İhsan Gürol Demirtaş'



