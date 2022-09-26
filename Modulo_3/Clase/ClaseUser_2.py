class User:
    """This class defines the behavior and state of a User. Basically, it tries to represent a User in the real life."""

    name = None
    email = None
    phoneNumber = None
    password = None

    def __init__(self, name, email, phoneNumber, password):
        """
            Constructor that ask for the below fields:
            name
            email
            phoneNumber
            password
        """
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.password = password

    def login(self, email: str = None, password: str = None, name: str = None) -> None:
        """Login that requested the user's email/name and password to be validated"""
        if email and password:
            if self.email == email and self.password == password:
                print(f"Bienvenido {self.name}")
            else:
                print("El email y/o contraseña proporcionados son incorrectos")
        elif name and password:
            if self.name == name and self.password == password:
                print(f"Bienvenido {self.name}")
            else:
                print("El nombre de usuario y/o contraseña proporcionados son incorrectos")
        else:
            print("Bienvenido. Aún no inicias sesión, para continuar por favor ingresa tus credenciales")


u1 = User('Abraham', 'abraham@hotmail.com', '2222222222', 'Admin123')
u1.login('abraham@hotmail.com', 'Admin123')
u1.login(name='Abraham', password='Admin123')
u1.login(name='Abraham')
u1.login(email='abraham@hotmail.com')
u1.login(password='Admin123')
u1.login()
print(User.phoneNumber)#Este es un atributo de clase
print(u1.phoneNumber)#Este es un atributp de instancia
User.phoneNumber = '3333333333'
u1.phoneNumber = '4444444444'
print(User.phoneNumber)#Este es un atributo de clase
print(u1.phoneNumber)#Este es un atributp de instancia