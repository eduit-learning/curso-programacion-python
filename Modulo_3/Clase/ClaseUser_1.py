#Antes de empezar con este médulo primero se debe crear un virtual environment
#1. Primero para saber en qué venv estoy puedo ejecutar
# import sys
# print(sys.prefix)
#2. Si queremos visualizar los paquetes que tenemos instalados antes de virtualenv podemos ejecutar "pip list"
#3. Instalamos virtualenv para poder trabajar con él: "pip install virtualenv"
#4. Validamos los paquetes instalados "pip list"
#5. Para crear un virtualenv ejecutamos: py -m venv <nombre del venv> en este caso "py -m venv ejemplos_modulo-3"
#6. Posiblemente Visual Studio Code te pregunte si quieres cambiarte al nuevo ambiente creado. Da click en "Yes/Sí"
#7. Para activar el venv creado debes ejecutar: env\Scripts\activate.bat, en este caso ejemplos_modulo-3/Scripts/activate.bat
#8. En caso de que VS Code no te sugiera el cambio de interprete, puede hacerlo desde la paleta de comandos (Ctrl + Shift + P)
# Seleccionar "Python: Select Interpreter" y seleccionar el venv creado anteriormente
#9. Ahora puedes inatalar los paquetes y módulos que quieras utilizar en tu código
#11. Para desactivar el venv creado debes ejecutar: env\Scripts\activate.bat, en este caso ejemplos_modulo-3/Scripts/deactivate.bat
#12. Para eliminarlo debes borrarlo físicamente

class User:
    """This class defines the behavior and state of a User. Basically, it tries to represent a User in the real life."""
    #La línea de código anterior es un Docstring. Si prestas atención no está asociado a una variable y
    #se abre y se cierra con 3 comillas dobles (también pueden ser comillas simples). Se puede colocar
    #justo después de una clase o justo después de funciones y sirven para documentar el código.

    name = 'Not assigned yet'
    email = None
    phoneNumber = None
    password = None

    def __init__(self):
        """Constructor without parameters"""
        name = 'Not assigned yet'
        email = 'Not assigned yet'
        phoneNumber = 'Not assigned yet'
        password = 'Not assigned yet'

    #Python no soporta multiples constructores. En este caso, el contructor de abajo sobrescribe al de arriba.
    #Es decir, el contructor que no recibe parámetros no podrá utilizarse.
    def __init__(self, name, email, phoneNumber, password):
        """
            Constructor que recibe los siguientes parámetros:
            name
            email
            phoneNumber
            password
        """
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.password = password

    def login(self, email, password):
        """Login that requested the user's email ans password to be validated"""
        if self.email == email and self.password == password:
            print(f"Bienvenido {self.name}")
        else:
            print("El nombre de usuario y/o contraseña proporcionados son incorrectos")

    ##La función debajo de este comentario está "comentada", esto es porque debido a que en Python las variables
    ##y los parámetros no son tipados (pueden recibir cualquier tipo de dato) la sobrecarga de métodos no
    ##funciona cuando la cantidad de parámetros es distinta, cuando la cantidad de parámetros son iguales
    ##la "sobrecarga" del método sobrescribe al método anterior. En este caso el método de abajo sobrescribe al
    ##método de arriba
    #def login(self, name, password):
    #    """Login that reuested the user's name ans password to be validate"""
    #    if self.name == name and self.password == password:
    #        print(f"Bienvenido {self.name}")
    #    else:
    #        print("El nombre de usuario y/o contraseña proporcionados son incorrectos")

#Debo llamar al constructor con parámetros porque el que no recibe parámetros fue sobreescrito.
u1 = User('Abraham','abraham@hotmail.com','2222222222','Admin123')
print(u1.name)
print(User.name)
User.name = 'Abraham'
print(User.name)
u1.login('abraham@hotmail.com','Admin1234')