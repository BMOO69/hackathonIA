from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from chatbotApp import views
##from chatbotApp import views

urlpatterns =[

    path('',views.saludo, name= 'chat'),
    path('chat/',views.chat_view, name='chat2'),
    path('refresh_chat/', views.refresh_chat_view, name='refresh_chat'),
    path('enviar/', views.send_message, name='enviar'),

    path('buscar/', views.buscar),

]


