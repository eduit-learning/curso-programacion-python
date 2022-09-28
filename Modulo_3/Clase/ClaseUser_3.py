#Para este ejemplo de debe instalar ".\pip.exe install multipledispatch" Asegurate de estar en la carpeta "Scripts"
#del vend creado
#Para desinstalarlo solo debes ejecutar ".\pip.exe uninstall multipledispatch"
from multipledispatch import dispatch

class User:
    """This class defines the behavior and state of a User. Basically, it tries to represent a User in the real life."""

    name = None
    email = None
    phoneNumber = None
    password = None

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

    @dispatch()
    def login(self) -> None:
        """Basic login without parameters"""
        print("Bienvenido. Aún no inicias sesión, para continuar por favor ingresa tus credenciales")

    @dispatch(str, str)
    def login(self, email: str, password: str) -> None:
        """Login that requested the user's email ans password to be validated"""
        if self.email == email and self.password == password:
            print(f"Bienvenido {self.name}")
        else:
            print("El nombre de usuario y/o contraseña proporcionados son incorrectos")

    #@dispatch(str, str)
    #def login(self, name, password):
    #    """Login that reuested the user's name ans password to be validate"""
    #    if self.name == name and self.password == password:
    #        print(f"Bienvenido {self.name}")
    #    else:
    #        print("El nombre de usuario y/o contraseña proporcionados son incorrectos")

    def __add__(self, o: object) -> str:
        return f'{self.name} - {o.name}'
    
    def __gt__(self, o: object) -> bool:
        if(self.name > o.name):
            return True
        return False
    
    def __lt__(self, o: object) -> bool:
        if(self.name < o.name):
            return True
        return False
    
    def __eq__(self, o: object) -> bool:
        if(self.name == o.name):
            return True
        return False


##u1 = User('Abraham', 'abraham@hotmail.com', '2222222222', 'Admin123')
##print(u1.name)
##u1.login() 
##u1.login('abraham@hotmail.com', 'Admin123')
##
##u2 = User('Pedro', 'pedro@hotmail.com', '3333333333', 'Admin123')
##print(u1 + u2)
##print(u1 > u2)
##print(u1 < u2)
##print(u1 == u2)
##u2.name = 'Abraham'
##print(u1 == u2)

#   Operator	Magic Method
#   +	__add__(self, other)
#   –	__sub__(self, other)
#   *	__mul__(self, other)
#   /	__truediv__(self, other)
#   //	__floordiv__(self, other)
#   %	__mod__(self, other)
#   **	__pow__(self, other)
#   >>	__rshift__(self, other)
#   <<	__lshift__(self, other)
#   &	__and__(self, other)
#   |	__or__(self, other)
#   ^	__xor__(self, other)

#   Operator	Magic Method
#   <	__lt__(self, other)
#   >	__gt__(self, other)
#   <=	__le__(self, other)
#   >=	__ge__(self, other)
#   ==	__eq__(self, other)
#   !=	__ne__(self, other)

#   Operator	Magic Method
#   -=	__isub__(self, other)
#   +=	__iadd__(self, other)
#   *=	__imul__(self, other)
#   /=	__idiv__(self, other)
#   //=	__ifloordiv__(self, other)
#   %=	__imod__(self, other)
#   **=	__ipow__(self, other)
#   >>=	__irshift__(self, other)
#   <<=	__ilshift__(self, other)
#   &=	__iand__(self, other)
#   |=	__ior__(self, other)
#   ^=	__ixor__(self, other)