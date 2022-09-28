from django.shortcuts import render,reverse,redirect

# Create your views here.
from cart.cart import Cart
from shop.models import Category, Product, Slider

from django.conf import settings
from django.core.mail import send_mail

from yoga.models import kvvk


def index(request):

    sliders = Slider.objects.all()
    all = Product.objects.filter(index=True).order_by('?')
    cate = Category.objects.filter(up__contains='bal')
    oil = Category.objects.filter(up__contains='zeytin')
    bee = Category.objects.filter(up__contains='arı')
    recel = Category.objects.filter(up__contains='reçel')
    area = Category.objects.filter(up__contains='yöre')
    heal = Category.objects.filter(up__contains='sağlık')
    badem = Category.objects.filter(up__contains='badem')

    print(cate)
    pdf = kvvk.objects.all()

    cart = Cart(request)
    print(request.user)
    print(cate)
    context = {
        'cate':cate,
        'badem':badem,
        'oil':oil,
        'bee':bee,
        'recel':recel,
        'area':area,
        'heal':heal,
        'cart':cart,

        'pdf':pdf,
        'all':all,
        'sliders':sliders

    }
    return render(request,'central/index.html',context)




def about(request):
    cart = Cart(request)

    context = {
        'cart': cart
    }
    return render(request,'central/about.html',context)


def mentor(request):
    cart = Cart(request)
    if 'btnSubmit' in request.POST:
        if True:
            hotel= 'Turban/İletişim Formu'
            name = request.POST.get('name')
            email = request.POST.get('email')
            info = request.POST.get('info')

            subject = 'Costumer Contact Messages'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,"djangomarmaris@gmail.com"]
            contact_message = "Name:%s\nEmail:%s\nHotel:%s\nInfo:%s" % (
                name,
                email,
            hotel,
            info)
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
        return redirect('/')

    context = {
        'cart': cart
    }
    return render(request,'central/mentor.html',context)

def share(request):
    cart = Cart(request)
    if 'btnSubmit' in request.POST:
        if True:
            name = request.POST.get('name')
            email = request.POST.get('email')
            info = request.POST.get('info')

            subject = 'Costumer Contact Messages'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,"djangomarmaris@gmail.com"]
            contact_message = "Name:%s\nEmail:%s\nInfo:%s" % (
                name,
                email,
            info)
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
        return redirect('/')
    context = {
        'cart': cart
    }
    return render(request,'central/share.html',context)

def question(request):
    cart = Cart(request)

    context = {
        'cart': cart
    }
    return render(request,'central/question.html',context)



def yoga(request):
    cart = Cart(request)

    context = {
        'cart': cart
    }
    return render(request,'central/yoga.html',context)


def contact(request):
    cate = Category.objects.filter(up__contains='bal')
    oil = Category.objects.filter(up__contains='zeytin')
    bee = Category.objects.filter(up__contains='arı')
    recel = Category.objects.filter(up__contains='reçel')
    area = Category.objects.filter(up__contains='yöre')
    heal = Category.objects.filter(up__contains='sağlık')
    badem = Category.objects.filter(up__contains='badem')
    if 'btnSubmit' in request.POST:
        if True:
            name = request.POST.get('name')
            email = request.POST.get('email')
            info = request.POST.get('info')
            case = request.POST.get('case')
            phone = request.POST.get('phone')
            mesaj = request.POST.get('mesaj')

            subject = 'Costumer Contact Messages'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,"djangomarmaris@gmail.com"]
            contact_message = "Name:%s\nEmail:%s\nInfo:%s\nCase:%s\nPhone:%s\nMessages:%s" % (
                name,
                email,
            info,
            case,
            phone,
            mesaj)
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
        return redirect('/')

    context = {
        'cate': cate,
        'badem': badem,
        'oil': oil,
        'bee': bee,
        'recel': recel,
        'area': area,
        'heal': heal,


    }
    return render(request,'central/contact.html',context)

############################################################################


from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from cart.cart import Cart
from  cart.forms import CartAddProductForm
from shop.models import Category,Product



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

    article = get_object_or_404(Product,slug=slug)


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





