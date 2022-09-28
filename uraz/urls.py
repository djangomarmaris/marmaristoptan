"""uraz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from yoga import views
from orders.views import *
from shop.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/',include('django.conf.urls.i18n')),
    path('webhooks/', webhook, name='webhooks'),
]
urlpatterns += i18n_patterns (
    path('',views.index,name='index'),



    path('cart/',include('cart.urls', namespace='cart')),
    path('iletisim/',views.contact,name='contact'),
    path('marmaris/<str:category_slug>/', views.Show, name='product_list_by_show'),
    path('<str:slug>/', views.product_detail, name = 'product_detail'),
    path('list/', views.product_list, name='product_list'),path('iletisim/',views.contact,name='iletişim'),
    path('order/', include('orders.urls',namespace='orders')),
    path('shop/',include('shop.urls', namespace='shop')),
    path('user/',include("user.urls")),
    #path('marmaris/',include("yoga.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    prefix_default_language=False
)
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)