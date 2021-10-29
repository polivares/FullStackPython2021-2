# Paquetes y modulos
# Utilizacion de un paquete de python
import numpy as np
# Utilizacion de un paquete/modulo creado por nosotros
import mypackage.modulo1 as md1

a = np.ones(20) # Esto crea un arreglo numpy de tamano 20 con puros unos
print(a)
b = np.arange(0, 1, 0.1)
print(b)
print(md1.suma(5, 3))

# Funciones con argumentos variables
def suma(a, b, c=0):
    return a+b

print(suma(3,5))
# que ocurre si queremos definir ahora una suma de tres numeros?
# Opciones: crear una nueva funcion, o modificar la anterior para que opere con dos y tres numeros
def suma3(a,b,c):
    return a+b+c
# Que pasa si ahora queremos una suma para 4 numeros... y para 5,... y para 6...
# ... ya me entienden...
# Primera forma para trabajar con argumentos variables: *args
print("Suma con Args")
def sumaArgs(*args):
    # Cuando definimos *args, lo que estamos indicando es que el argumento de entrada es 
    # una tupla de largo variable
    res = 0
    for i in args:
        res +=i 
    return res
print(sumaArgs(3, 5))
print(sumaArgs(3,6,2))
print(sumaArgs(5,4,7,2,8))

# Segunda forma para trabajar con argumentos variables: **kwargs
print("Suma con Kwargs")
def sumaKwArgs(**kwargs):
    # Cuando definimos **kwargs, lo que estamos indicando es que el argumento de entrada es
    # un diccionario de largo y llaves variables
    res = 0
    print(kwargs)
    for v in kwargs.values():
        res += v
    return res

print(sumaKwArgs(pera=10,z=20, a=15, hola=40 ))

# Puedo juntar parametros de entrada fijos, parametros de entrada con valor por omision,
# parametros variables con *args y parametros variables con **kwargs??? 
# Si, de la forma que tu quieras!

def sumaAlmenos2(a,b,*args):
    res = a+b
    for i in args:
        res += i 
    return res 

print(sumaAlmenos2(1,3, 5))


def crearGrupo(**kwargs):
    if "nombre1" in kwargs.keys():
        print("El nombre del integrante 1 es:", kwargs["nombre1"])
    if "nombre2" in kwargs.keys():
        print("El nombre del integrante 2 es:", kwargs["nombre2"])
    if "nombre3" in kwargs.keys():
        print("El nombre del integrante 3 es:", kwargs["nombre3"])

crearGrupo(nombre3="Maria", nombre1="Pedro")

def datosUsuario(**kwargs):
    if "edad" in kwargs.keys():
        print("La edad es ", kwargs["edad"])
    if "nombre" in kwargs.keys():
        print("El nombre es ", kwargs["nombre"])

datosUsuario(nombre="Patricio", edad=35)
datosUsuario( edad=35, nombre="Patricio")
datosUsuario( edad=35)

