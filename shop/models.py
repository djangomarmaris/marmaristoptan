import os
from PIL import Image, ExifTags
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

MODEL = (
        ('Bal Çeşitleri', 'Bal Çeşitleri'),
        ('Arı Ürünleri', 'Arı Ürünleri'),
        ('Reçel & Pekmez', 'Reçel & Pekmez'),
        ('Yöresel Ürünler', 'Yöresel Ürünler'),
        ('Zeytin & Zeytinyağı', 'Zeytin & Zeytinyağı'),
        ('Sağlık Ürünleri', 'Sağlık Ürünleri'),
        ('Badem Ürünleri', 'Badem Ürünleri'),
        )



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, null=True, blank=True)
    up = models.CharField(max_length=100, choices=MODEL, default='Ürün Üst Modeli Nedir?')
    slug = models.SlugField(max_length=100, db_index=True, unique=True)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('product_list_by_show', args=[self.slug])



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE,blank=True,null=True)
    product_no = models.CharField(max_length=100,default='Ürün Kodu Giriniz')
    name = models.CharField(max_length=200,default='Ürün Kodu Giriniz')
    slug = models.SlugField()
    image = models.CharField(max_length=200,default='Ürün Kodu Giriniz')


    price = models.CharField(max_length=200,default='Ürün Kodu Giriniz')

    stock = models.CharField(max_length=200,default='Ürün Kodu Giriniz')
    index = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    seo = models.CharField(max_length=500,default="Seo için Bilgi Giriniz.")
    key = models.CharField(max_length=550,default="Keyword için Giriş")


    class Meta:
        ordering = ('created',)
        index_together = (('id', 'slug',))

    def __str__(self):
        return self.name


    def get_cat_list(self):
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i]='/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]



    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])





class Slider(models.Model):
    h1 = models.CharField(max_length=200, default='Ürün Kodu Giriniz')
    h2 = models.CharField(max_length=200, default='Ürün Kodu Giriniz')
    product  = models.CharField(max_length=200, default='Ürün Kodu Giriniz')
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)



    def __str__(self):
        return self.h1




