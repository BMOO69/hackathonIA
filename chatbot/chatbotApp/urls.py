from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from chatbotApp import views
##from chatbotApp import views

urlpatterns =[

    path('',views.saludo, name= 'chat'),

]


