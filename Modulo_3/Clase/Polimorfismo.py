class Perro:
    def sonido(self):
        print('Guauuuuu!!!')
class Gato:
    def sonido(self):
        print('Miaaauuuu!!!')
        
class Vaca:
    def sonido(self):
        print('Múuuuuuuu!!!')

def a_cantar(animales):
    for animal in animales:
        animal.sonido()

perro = Perro()
gato = Gato()
gato_2 = Gato()
vaca = Vaca()
perro_2 = Perro()
granja = [perro, gato, vaca, gato_2, perro_2]
a_cantar(granja)