from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views




app_name = 'yoga'


urlpatterns =[
    path('',views.index,name ='index'),
    #path('about/',views.about,name='about'),
    #path('mentor/',views.mentor,name='mentor'),
    #path('share/',views.share,name='share'),
    #path('yoga/',views.yoga,name='yoga'),
    path('contact/',views.contact,name='contact'),

]


