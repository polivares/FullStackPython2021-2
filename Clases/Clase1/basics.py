# Este es un comentario de una sola linea
# Esta es la segunda linea de tu comentario

''' Esto de aca
es un comentario
que ocupa varias
lineas
'''

# Variables
x=2 # Esta de aca es la variable x y tiene asignada un valor de 2
y=5 # Esta seria la variable y
z=x+y # Creamos la variable z y le asignamos el resultado de x + y. z = 7
print(z) # Esto muestra por la terminal el valor de la variable z

# Cosas que se pueden almacenar en variables python (básico)
a1 = 10 # Numeros enteros. Almacena el entero 10 (integer - int)
a2 = 15.3 # Numeros decimales (reales). Almacena el numero flotante 15.3 (flotantes - float)
a3 = "Este es un texto creado con comillas dobles" # Strings. Almacena el texto indicado (strings - str)
a4 = 'Este es un texto creado con comillas simples' # Tambien es un string
a5 = True # Booleanos (valores de verdadero (True) y falso (False)). Almacena valor True. (booleanos - bool)
a6 = 3.3 + 5.1j # Numeros completos. Estos tiene una parte real y una parte imaginaria (acompañada de una j). (complejos - complex)

print(a1, a2, a3, a4, a5, a6) # Muestra los datos almacenados en todas las variables por la terminal

''' 
Quiero escribir por pantalla: 
El valor de la variable a1 es <aqui va el valor de a1> y el valor de a2 es <aqui va el valor de a2>
Ej:
El valor de la variable a1 es 10 y el valor de a2 es 15.3
'''
print("El valor de la variable a1 es", a1, "y el valor de la variable a2 es", a2)
print("El valor de la variable a1 es " + str(a1) + " y el valor de la variable a2 es " + str(a2))
print("El valor de la variable a1 es %d y el valor de la variable a2 es %f " % (a1, a2))
print(f"El valor de la variable a1 es {a1} y el valor de la variable a2 es {a2}")