# Este es el archivo encargado de codificar las funciones de vista en Django (parecido a lo que
# hacía nuestro archivo app.py en Flask)

# Por cada vista que yo quiera crear, debo codificar una función de vista (OJO: con sintáxis de Django)

from django.shortcuts import HttpResponse

def index(request):
    # Lo único que queremos hacer es mostrar un texto html
    return HttpResponse('<h1>Bienvenido a MyEnterprise s.a. </h1>')
