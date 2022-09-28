from Clasecasa import casa
# Escribir una función que reciba como parámetro otra función y una lista, y devuelva otra lista con el resultado
# de aplicar la función dada a cada uno de los elementos de la lista.
# function(paraA:fn, pamb:list) pamb = ['a','b','c','d','e']
#    Aplicar la parA a los elementos de pamb
#    return el resultado


def aplica_funcion_lista(funcion, lista):
    '''Función que aplica una función a todos los elementos de una lista.

    Parámetros:
        funcion: Es una función.
        lista: Es una lista con valores que se pasarán como argumentos a funcion.
    Devuelve:
        Una lista con el resultado de aplicar la función a los valores de la lista.
    '''
    l = []
    for i in lista:
        l.append(funcion(i))
    return l


def cuadrado(n):
    return n * n


print(aplica_funcion_lista(cuadrado, [1, 2, 3, 4]))

print(aplica_funcion_lista(lambda n: n*n, [1, 2, 3, 4]))#lambda parámetro: return

# Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
# "Hola a todos equipo de VW" -> {"Hola":4, "a":1, "todos":5, ...}


def length_words(sentence):
    '''
    Función que recibe una frase y devuelve un diccionario con las palabras que contiene y su longitud.
    Parámetros:
        sentence: Es una cadena de caracteres con una frase.
    Devuelve:
        Un diccionario con pares palabra:longitud donde palabra son las palabras que contiene la frase sentence.
    '''
    words = sentence.split()
    # Map aplica la función del primer parámetro a los objetos del segundo parámetro
    lengths = map(len, words)
    #print(list(lengths))
    print(tuple(zip(('A', 'B', 'C'), (1, 2, 3, 4))))
    return dict(zip(words, lengths)) # zip realiza el join de dos tuplas


print(length_words('Hola a todos equipo de VW'))


# Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:
# [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garage': True, 'zona': 'A', 'precio': 23423.334},
#{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garage': True, 'zona': 'B', 'precio': 23423.334},
#{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garage': False, 'zona': 'A', 'precio': 23423.334},
#{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garage': True, 'zona': 'B', 'precio': 23423.334},
# {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garage': False, 'zona': 'A', 'precio': 23423.334}]
# Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado.
# La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con
# los inmuebles cuyo precio sea menor o igual al proporcionado. Debe hacerlo con clases.
class Inmueble:
    def __init__(self, anio: int, metros: float, habitaciones: int, garage: bool, zona: str, precio: float) -> None:
        self.anio = anio
        self.metros = metros
        self.habitaciones = habitaciones
        self.garage = garage
        self.zona = zona
        self.precio = precio



class SearchEngine:
    def __init__(self, buildingList: list) -> None:
        self.buildingList = buildingList

    def search_best_price(self, price: float) -> list:
        return map(lambda x: x if x.precio <= price else None, self.buildingList)

searcher = SearchEngine([Inmueble(2022, 80.32, 2, False, 'B', 800000),
Inmueble(2000, 200, 2, True, 'B', 2000000.00),
Inmueble(2020, 135.48, 2, True, 'B', 1500000.00),
Inmueble(2010, 101.12, 2, False, 'B', 1200000)])

print('\n\nInmuebles disponibles...\n')
for i in searcher.search_best_price(1250000):
    print(f'Precio: ${i.precio:,.2f}\nAño: {i.anio}\nMetros: {i.metros:,.2f}\nHabitaciones: {i.habitaciones}\n¿Tiene garage?: {i.garage}\nZona: {i.zona}\n') if i != None else print()
#El if en linea siempre debe llevar la estructura: operación[si condición es verdadera] if condición else operación [si condición es falso]

print(dir(searcher))
print('**************************************')
print(dir(SearchEngine))