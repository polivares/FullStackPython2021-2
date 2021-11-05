dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
} 


def printInfo(diccionario):
    # A partir de un dict mostrar: cada llave acompanada de largo de la lista y sus elementos
    # Primero, voy a recorrer los elementos del diccionario
    for k, v in diccionario.items():
        # Ahora muestro la llave, el largo
        print(k, len(v))
        # Ahora recorro la lista
        for i in v:
            print(i)

printInfo(dojo)


class A:
    def __init__(self, inicial):
        self.i = inicial # Esto es un número

    def sumaI(self, otroObjetoA):
        # Tener presente que la variable otroObjetoA es tambien de la clase A
        self.i += otroObjetoA.i

# Ahora creamos los objetos
a1 = A(100) # Esto inicializa el objeto a1 de la clase A con i=100
a2 = A(200) # Esto inicializa el objeto a2 de la clase A con i=200

print(a1.i, a2.i) # 100 200
a1.sumaI(a2) # En esta linea, cuando vemos el codigo de la clase, self representa a1 y otroObjetoA representa a2
# En este llamado, se actualiza el atributo i de a1 como 300
a2.sumaI(a1) # En este caso, el atributo i de a2 es 500
print(a1.i, a2.i)
