# Definicion de clases
class Perro:
    # Aca dentro ira los estados de cada perro (como variables)
    # Y sus funcionalidades (como funciones)

    # Respecto al estado: que cosas me interesan de los perritos?
    # Nombre, edad, raza, fecha de ultima vacuna
    def __init__(self, name, age, r, date_v):
        # Con esto, tenemos definido su estado (al menos inicialmente)
        self.nombre = name
        self.edad = age
        self.raza = r 
        self.f_vacunacion = date_v
    # A continuacion, escribiremos todas las funcionalidades que puede realizar esta clase
    # Recordemos que las funcionalidades quedan definidas como funciones internas
    def cumple(self):
        self.edad += 1

    def updateFVacunacion(self, new_date_v):
        self.f_vacunacion = new_date_v


# Ya tenemos definida nuestra clase Perro. Como creamos objetos a partir de esta clase?
# Recordemos que un objeto es algo "concreto" dentro del grupo que define la clase
a = 10 # Esto crea una variable que almacena un entero
perroA = Perro("Gandalf", 5, "Bichon", '30-11-2021')
perroB = Perro("Toto", 5, "Poodle", '15-12-2021')

# Cual es el nombre del perroA?
print(perroA.nombre) # Esto accede al nombre que hayamos definido en perroA (Gandalf)
print(perroB.nombre)

# Como utilizas los metodos internos de una clase a partir de su objeto?
perroA.cumple() # Esta linea de aca ejecuta el metodo cumple en el objeto perroA ("Gandalf")
print(f"La edad de {perroA.nombre} es ", perroA.edad) # Esto debe retornar 6

# Herencia
# Es la creacion de una clase base que agrupa aquellos elementos comunes de una
# o mas clases. Esto permite agrupar caracteristicas comunes entre dichas clases
class Felino:
    def __init__(self, nombre, edad, sonido):
        self.nombre = nombre
        self.edad = edad
        self.sonido = sonido
    
    def emitirSonido(self):
        return self.sonido
    

class Gato(Felino):
    # En este punto, debido a la herencia, la clase Gato, puede hacer
    # TODO lo que puede hacer la clase Felino. 
    def __init__(self, nombre, edad, dueno):
        Felino.__init__(self, nombre, edad, "Miau")
        self.dueno = dueno
    
class Leon(Felino):
    # Nuevamente, la clase Leon, al igual que la clase Gato, tambien puede
    # hacer lo mismo que un Felino
    def __init__(self, nombre, edad):
        Felino.__init__(self, nombre, edad, "Grrrr")

cat = Gato("Garfield", 7, "John")
lion = Leon("Leoncio", 10)

print(cat.emitirSonido())
print(lion.emitirSonido())

