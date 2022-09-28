import os

os.system('cls')

try:
    print("De esta manera controlo una Excepción")
except:
    print("Acá controllo una excepción")

try:
    customList = [1, 2, 3]
    print(customList[5])
except:
    print("Ocurrió un error")

try:
    customList = [1, 2, 3]
    print(customList[5])
except IndexError as ex:
    print(f"Ocurrió un error al intentar acceder al índice de la lista. {ex}")
except ValueError as ex:
    print(
        f"El valor proporcionado para acceder al elemento de la lista es incorrecto. {ex}")
except Exception as ex:
    print(f"Ocurrió un error. {ex}")
finally:
    print("Esto siempre se ejecuta, no importa si ocurrió una excepción o no")

try:
    x = 0
    y = 2
    if (x == 0):
        raise ZeroDivisionError("No es posible dividir por 0")
except Exception as ex:
    print(f"Ocurrió un error. {ex}")

try:
    x = 0
    y = 2
    y/x
except Exception as ex:
    raise Exception(ex)

# https://docs.python.org/3/library/exceptions.html