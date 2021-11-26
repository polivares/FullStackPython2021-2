from django.shortcuts import render, redirect 

# Create your views here.
def index(request):
    # Cómo enviamos datos de contexto a nuestro html en el proceso de renderizado?
    # La variable que entrega contexto a nuestro renderizado es una sola variable (a diferencia de Flask)
    # de tipo diccionario. Las llaves de este diccionario van a representar los nombres de las variables
    # que serán utilizadas en nuestro proceso de renderizado. El valor asociado a cada llave, representa
    # el valor de esa variable
    context = {
        'nombre': 'Optimus Prime',
        'pos_cargo': 1,
        'amigos': ['Bumblebee', 'Ratchet', 'Ironhide']
    }
    return render(request, "index.html",context=context)

def solicitudes(request): # Vista que puede detectar solicitudes GET y POST
    context = {}
    # Primero vamos a detectar si la solicitud es de tipo GET
    if request.method == 'GET':
        # Al detectar una solicitud de tipo GET, voy a redirigir el tráfico a la vista del
        # formulario
        return redirect("/app1/form")
    elif request.method == 'POST':   # Acá detectaremos si la solicitud es de tipo POST
        print('Se detectó una solicitud de tipo POST')
        print(request.POST)
        print(request.POST["nombre"])
        # Si la solicitud es de tipo POST, agregaremos esto a nuestra variable de contexto
        context['solicitud'] = 'Esta solicitud es de tipo POST'
        # Desde el formulario form.html se enviaron los datos de nombre y pos_cargo.
        # Usaremos el nombre como un dato para indicar que el usuario inicio sesión
        request.session["nombre"] = request.POST["nombre"]
        return render(request, "solicitudes.html", context=context)

def form(request):
    return render(request, "form.html")