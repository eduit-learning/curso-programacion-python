class A:
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        self.afield = 'Este es un campo de la clase A'
    
    def printData(self):
        print(self.name)
        print(self.afield)
    
    def printAData(self):
        print('Imprimiendo desde la clase A')
        
class B:
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        self.bfield = 'Este es un campo de la clase B'
    
    def printData(self):
        print(self.description)
        print(self.bfield)
    
    def printBData(self):
        print('Imprimiendo desde la clase B')

class C(A, B): #Siempre tendrán mayor importancia los métodos de la primera clase que aparece en los paréntesis
    def __init__(self, name, description) -> None:
        super().__init__(name, description)

c1 = C('Clase c','Esta es la clase C')
c1.printData()
c1.printAData()
c1.printBData()