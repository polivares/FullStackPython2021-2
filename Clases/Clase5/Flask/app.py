from flask import Flask, render_template, request  # Importar Flask para que permita crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')
@app.route('/hola', methods=["GET","POST"])          # El decorador "@" asocia la ruta con la función siguiente (enrutador)
def hello_world():          # Funciones views
    if request.method == "GET":
        return render_template("index.html", nombreUsuario="Patricio", numero=5, edad=20)  # Retorna la cadena 'Hello World!' como respuesta    
        # Esta función de tipo vista, por omisión responde a solicitudes de tipo GET
    else:
        print("Entré por un POST")
    

# Por cada página dentro de mi web, hago una función que se encargue de mostrarla

if __name__=="__main__":   # Asegúrese de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True)    # ejecuta la aplicación en modo depuración