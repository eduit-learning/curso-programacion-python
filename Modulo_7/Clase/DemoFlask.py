#1. Valida que en el entorno global tengas instalado el paquete "virtualenv". Puedes hacerlo con "pip list"
#2. Si no tienes instalado el paquete "virtualenv" puedes instalar con "pip install virtualenv"
#3. Crea un entorno virtual con el nombre "demo_flask" con "py -m venv demo_flask". Puede ser en el path de tu elección
#4. Esto creará el dirctorio "[path seleccionado]\demo_flask". en este ejemplo:
# "C:\EduIT_Curso_Python\Modulo_7\Clase\demo_flask"
#5. Selecciona el interprete correcto en VS Code apuntando al vend creado y abre una consola nueva a partir de ese interprete para que active
# el venv creado.
#6. Asegurandote que la consola de VS Code está trabajando con el ambiente creado. Instala el paquete de Flask
# con "pip install flask"

import pyodbc
import os
import json
from flask import Flask, request, redirect, url_for, jsonify, render_template #Importa las clases/objetos que se requieren para trabajar con Flask

class User:
    def __init__(self, userID, name, lastName, email, userName, password, country, language, roleID) -> None:
        self.userID = userID
        self.name = name
        self.lastName = lastName
        self.email = email
        self.userName = userName
        self.password = password
        self.country = country
        self.language = language
        self.roleID = roleID
    
    def toJSON(self):
        return json.dumps(self, default = lambda o: o.__dict__, sort_keys = False, indent = 4)
        

class SQLOperations:
    def __init__(self) -> None:
        self.connectionString = ("Driver={SQL Server Native Client 11.0};"
                                 "Server=localhost\SQLEXPRESS,1433;Database=EduIT;UID=sa;PWD=Admin123;")

    def execute_reader(self, query: str) -> list:
        items = []
        cnxn = pyodbc.connect(self.connectionString)
        cursor = cnxn.cursor()
        for item in cursor.execute(query):
            items.append(User(item[0], item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[0]).toJSON())
        cursor.close()
        cnxn.close()

        return items

    def execute_query(self, query: str) -> None:
        cnxn = pyodbc.connect(self.connectionString)
        cursor = cnxn.cursor()
        count = cursor.execute(query)
        print(f"Se afectaron {count.rowcount} líneas")
        cnxn.commit()
        
        cursor.close()
        cnxn.close()

#Crea una instancia de la clase Falsk que recibe como parámetro el paquete de la aplicación donde se está ejecutando
#En este ejemplo el nombre del paquete es "DemoFlask" ya que es el nombre del archivo y __name__ contiene el valor
#__main__ ya que lo estámos ejecutando en la "raíz" del paquete.
app = Flask(__name__)

@app.route('/') #Indica la ruta por la cuál accederemos a esta operación
def hello_world():
    return 'Hola, mundo123!'

def hello_world3():
    return 'Hola, mundo1234!'

#Este método debido a quew también apunta a la raíz es ignorado ya que previamente hay otro método que apunta también a la raíz
#y Flask trabaja con el primero que encuentre
@app.route('/h')
def hello_world2():
    return 'Hola, mundo1234! - ' + hello_world3()

@app.route('/print-message')
def print_message():
    message = request.args.get('message')
    message2 = request.args.get('message2')
    message3 = request.args.get('message3')
    return f'Bienvenido a Flask: {message} - {message2} - {message3}'

@app.route('/greetings/<string:name>/<string:lastName>')
def greetings(name:str, lastName:str):
    return f'Hola {name} - {lastName}'

@app.route('/print-age/<int:age>')
def print_age(age:int):
    print(type(age))
    return f'Tu edad es: {age} años'

#Los tipos de datos que puedo poner en los parámetros son:
#string: Es el conversor por defecto. Acepta cualquier cadena que no contenga el carácter ‘/’.
#int: Acepta números enteros positivos.
#float: Acepta números en punto flotante positivos.
#path: Es como string pero acepta cadenas con el carácter ‘/’.
#uuid:  Acepta cadenas con formato UUID.

@app.route('/hello-world', methods = ['POST'])
def hello_world_post():
    return 'Hola, mundo desde POST!'

@app.route('/hello-world-delete', methods = ['DELETE'])
def hello_world_delete():
    return 'Hola, mundo desde DELETE!'

@app.route('/hello-world-put', methods = ['PUT'])
def hello_world_put():
    return 'Hola, mundo desde PUT!'

@app.route('/users')
def get_all_users():
    context = SQLOperations()
    result = context.execute_reader('SELECT * FROM [User]')
    resultJson = f"[{','.join(result)}]"
    return resultJson

@app.route("/post")
def show_post():
    #El método "render_template" siempre buscará el path pasado como primer parámeto en la capreta "Templates"
    return render_template("html/index.html", html_title='Esta es una página con Flask', html_subtitle = 'Este es el subtítulo')

@app.route("/post2")
def show_post2():
    #El método "render_template" siempre buscará el path pasado como primer parámeto en la capreta "Templates"
    return render_template("html/index.html", html_user = User('1','Pedro','qwe', 'qwe', 'qwe', 'qwe', 'qwe', 'qwe', '2'))

#7. Flask viene con un servidor para probar las aplicaciones (jinja2). Para lanzar la aplicación haciendo uso de este
# servidor, debes ejecutar el comando flask o bien python -m.
#8. Para hacerlo debemos indicarle al servidor qué aplicación debe lanzar declarando
# la variable de entorno FLASK_APP en el archivo "activate.ps1" si usas VS Code y en el archivo "activate.bat"
# si usas el CMD: set "FLASK_APP=[nombre del archivo].py", en este caso: set "FLASK_APP=DemoFlask.py". Recuerda que este archivo se encuentra en la carpeta "Scripts" del venv
# creado al inicio. Si modificas el archivo activate.ps1 la linea debe ser: $Env:FLASK_APP="DemoFlask.py" y se
# agrega antes de la firma del archivo
#9. Reinicias la terminal cerrandola y abriendola de nuevo.
#10. Ejecutamos la aplicación con: "python -m flask run". Asegurate de que la consola esté en el directorio donde
# se encuentra el archivo a ejecutar
#11. Si deseas activar el mono debug, debes agregar la variable de entorno set "FLASK_ENV=development" al archivo
# activate.bat o $Env:FLASK_ENV="development" al arechivo activate.ps1

#Escribir una operación que reciba como parámetro el ID de un usuario y muetre el detalle de ese usuario en una página HTML