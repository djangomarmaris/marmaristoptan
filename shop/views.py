from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from cart.cart import Cart
from  cart.forms import CartAddProductForm
from .models import Category,Product



def Show(request, category_slug = None):
    cart = Cart(request)
    cate = Category.objects.filter(up__contains='bal')
    oil = Category.objects.filter(up__contains='zeytin')
    bee = Category.objects.filter(up__contains='arı')
    recel = Category.objects.filter(up__contains='reçel')
    area = Category.objects.filter(up__contains='yöre')
    heal = Category.objects.filter(up__contains='sağlık')
    badem = Category.objects.filter(up__contains='badem')
    full = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('-id')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    contex= {
        'cart':cart,
        'category':category,
        'products':products,
        'full':full,
        'cate': cate,
        'badem': badem,
        'oil': oil,
        'bee': bee,
        'recel': recel,
        'area': area,
        'heal': heal,

    }

    return render(request,'shop/products/show.html',contex)





def product_list(request):
    me = CartAddProductForm()

    jet = Category.objects.filter(name__contains='jet')
    fly = Category.objects.filter(name__contains='fly')
    tur = Category.objects.filter(name__contains='turlar')
    adre = Category.objects.filter(name__contains='adrenalin')
    korsan = Category.objects.filter(name__contains = 'tekne')
    products = Product.objects.filter(available=True).order_by('?')

    return render(request, 'shop/products/list.html',{'products':products,
                                                      'me':me,'jet':jet,'fly':fly,'tur':tur,'adre':adre,'korsan':korsan})




def product_detail(request,slug):
    smiller = Product.objects.filter(available=True).order_by('?')
    cate = Category.objects.filter(up__contains='bal')
    oil = Category.objects.filter(up__contains='zeytin')
    bee = Category.objects.filter(up__contains='arı')
    recel = Category.objects.filter(up__contains='reçel')
    area = Category.objects.filter(up__contains='yöre')
    heal = Category.objects.filter(up__contains='sağlık')
    badem = Category.objects.filter(up__contains='badem')
    cart = Cart(request)
    product = get_object_or_404(Product, slug = slug , available=True)
    form = CartAddProductForm()

    article = get_object_or_404(Product,id=id)


    context = {
        'article':article,
        'cart':cart,
        'product':product,
        'form':form,
        'cate': cate,
        'badem': badem,
        'oil': oil,
        'bee': bee,
        'recel': recel,
        'area': area,
        'heal': heal,
        'smiller':smiller
    }

    return render(request,'shop/products/detail.html',context)





