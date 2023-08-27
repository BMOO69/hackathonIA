from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from chatbotApp.models import Menssage
# Create your views here.

def saludo(request):
   ## cadena = request.GET["mensajeUser"]
    return render(request, "chatbotApp/chat.html")

def vista(request):
    if request.method == 'POST':
        mensaje_user = request.POST.get('mensajeUser', '')  # Obtén el valor de mensajeUser
        # Haz algo con mensaje_user, como guardarlo en la base de datos o procesarlo de alguna manera.
    
    # Resto de la lógica de tu vista aquí

    return render(request, 'tu_template.html', context)

def prueba(request):
    mensje = "mensajeUser: %r " %request.GET[""]

def chat_view(request):
    messages = Menssage.objects.all()
    return render(request, 'chatbotApp/chat2.html', {'messages': messages})

def refresh_chat_view(request):
    messages = Menssage.objects.all()
    return render(request, 'chatbotApp/chat2.html', {'messages': messages})

def send_message(request):
    print(request.POST.get('message'))
    if request.method == 'POST':
        sender = 'Usuario'  # Puedes personalizar esto según tu lógica de autenticación
        content = request.POST.get('message')
        message = Menssage(sender=sender, content=content)

        message.save()
        # Resto de tu lógica de envío de mensajes
    return HttpResponseRedirect('chatbotApp/chat2.html')  # Redirige a la página del chat después de enviar el mensaje

def buscar(request):
    
    if request.method == 'POST':
        print(request.POST.get('message'))
        sender = "Usuario"
        content = request.POST.get('message')
        message = Menssage(sender= sender, content=content )
        message.save()
        
        mensaje = "mensaje: %r" %request.POST.get("message")
    
    return HttpResponse(mensaje)

