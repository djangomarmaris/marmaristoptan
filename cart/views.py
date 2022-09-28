from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib.auth.decorators import login_required

@require_POST
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product)
    return redirect('cart:cart_detail')



@login_required(login_url="user:login")

def cart_detail(request):
    cate = Category.objects.filter(up__contains='bal')
    oil = Category.objects.filter(up__contains='zeytin')
    bee = Category.objects.filter(up__contains='arı')
    recel = Category.objects.filter(up__contains='reçel')
    area = Category.objects.filter(up__contains='yöre')
    heal = Category.objects.filter(up__contains='sağlık')
    badem = Category.objects.filter(up__contains='badem')




    cart = Cart(request)

    context = {
        'cate': cate,
        'badem': badem,
        'oil': oil,
        'bee': bee,
        'recel': recel,
        'area': area,
        'heal': heal,
        'cart':cart

    }
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html',context)