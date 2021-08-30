
from django.db import models
from django import forms
from django.forms import SelectDateWidget

from shop.models import Product
from django.urls import reverse
import datetime
from django.contrib.auth.models import User




class Order(models.Model):
    first_name = models.CharField(max_length=50,verbose_name="İsim:")
    last_name = models.CharField(max_length=50,verbose_name="Soy İsim:")
    email = models.EmailField(verbose_name="Email Adresiniz:",default="")
    phone = models.CharField(max_length=11,verbose_name="Telefon :")
    tc = models.CharField(max_length=11,verbose_name="Tc No:")
    city = models.CharField(max_length=100,verbose_name="İl :")
    adress = models.CharField(max_length=100,verbose_name="Adres :")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    uniqid = models.CharField(max_length=11,verbose_name="Uniq id:")



    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())



class OrderItem(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="Alan")
    order = models.ForeignKey(Order, related_name='items', on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete = models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    created_date = models.DateTimeField(auto_now=True, verbose_name="Oluşturlma Tarihi")
    tokenCheck = models.CharField(max_length=36,verbose_name="Token check:", null=False, default=False)
    paid = models.BooleanField(default=False)



    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity





