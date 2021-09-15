
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





class ReturnData(models.Model):
    status = models.CharField(max_length=510,verbose_name="status:")
    systemtime = models.CharField(max_length=510,verbose_name="systemtime:")
    conversationİd = models.CharField(max_length=510,verbose_name="conversationİd:")
    price =  models.CharField(max_length=510,verbose_name="price:")
    paidPrice = models.CharField(max_length=510,verbose_name="paidPrice:")
    paymentid = models.CharField(max_length=510,verbose_name="paymentid:")
    binNumber = models.CharField(max_length=510,verbose_name="binNumber:")
    result_token = models.CharField(max_length=510,verbose_name="result_token:")
    payment_token = models.CharField(max_length=510,verbose_name="payment_token:")


    def __str__(self):
        return self.status



class WebhookData(models.Model):
    paymentConversation = models.CharField(max_length=510,verbose_name="paymentConversation:")
    merchant = models.CharField(max_length=510,verbose_name="merchant:")
    webhooktoken = models.CharField(max_length=510,verbose_name="webhooktoken:")
    status = models.CharField(max_length=510,verbose_name="status:")
    iyziReferenceCode = models.CharField(max_length=510,verbose_name="iyziReferenceCode:")
    iyziEventType = models.CharField(max_length=510,verbose_name="iyziEventType:")
    iyziEventTime =models.CharField(max_length=510,verbose_name="iyziEventTime:")


    def __str__(self):
        return self.status



class UserTokenData(models.Model):
    userlast = models.CharField(max_length=510)
    usertoken = models.CharField(max_length=510)


    def __str__(self):
        return self.usertoken