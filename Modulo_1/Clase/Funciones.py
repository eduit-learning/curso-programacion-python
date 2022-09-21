def multiplica_por_5(numero):
    print(f'{numero} * 5 = {numero * 5}')

print('Comienzo del programa')    
multiplica_por_5(7)
print('Siguiente')
multiplica_por_5(113)
print('Fin')

#######################################################################33
def cuadrado_de_par(numero):
    if not numero % 2 == 0:
        return
    else:
        print(numero ** 2)
    
cuadrado_de_par(8)
cuadrado_de_par(3)

#########################################################################
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
es_par(2)
es_par(5)

def cuadrado_y_cubo(numero):
    return numero ** 2, numero ** 3

cuad, cubo = cuadrado_y_cubo(4)
print(cuad)
print(cubo)