import os
import calendar
import datetime as dt
import time
import locale

os.system('cls')
locale.setlocale(locale.LC_ALL, 'es_MX')

# Escribir una función que determine si un año es bisiesto o no
def leap_year(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True
    return False


print('***Ejercicio 1 - Solución 1***')
print(f'¿El año 1900 es bisiesto? {leap_year(1900)}')
print(f'¿El año 2022 es bisiesto? {leap_year(2022)}')
print(f'¿El año 2026 es bisiesto? {leap_year(2026)}')
print(f'¿El año 1904 es bisiesto? {leap_year(1904)}')
print(f'¿El año 2024 es bisiesto? {leap_year(2024)}')
print(f'¿El año 2004 es bisiesto? {leap_year(2004)}')

print('\n***Ejercicio 1 - Solución 2***')
print(f'¿El año 1900 es bisiesto? {calendar.isleap(1900)}')
print(f'¿El año 2022 es bisiesto? {calendar.isleap(2022)}')
print(f'¿El año 2026 es bisiesto? {calendar.isleap(2026)}')
print(f'¿El año 1904 es bisiesto? {calendar.isleap(1904)}')
print(f'¿El año 2024 es bisiesto? {calendar.isleap(2024)}')
print(f'¿El año 2004 es bisiesto? {calendar.isleap(2004)}')

# Escribir una función que reciba como parámetro una fecha (Day/Month/Year) puede ser datetime.now y
# regrese qué día del año representa esa fecha. Por ejemplo 1/1/2020 = 1, 23/02/2022 = 54
print('\n***Ejercicio 2 - Solución 1***')
today = dt.datetime.now()
print(
    f'Hoy es el día "{(today - dt.datetime(today.year, 1, 1)).days + 1}" del año')

print('\n***Ejercicio 2 - Solución 2***')
print(f'Hoy es el día "{dt.datetime.now().strftime("%j")}" del año')

# Escribir una función que muestre el tiempo actual en milisegundos
print('\n***Ejercicio 3 - ¿Solución 1?***')
mseconds = int(round(time.time() * 1000))
print(
    f'La fecha de hoy es: {dt.datetime.now()} y eso representa {mseconds} milisegundos')
print(
    f'¿Pero si lo anterios lo convierto en años? {mseconds} / 1000 -> segundos / 60 -> minutos / 60 -> horas / 24 -> días / 365 -> años {mseconds/1000/60/60/24/365}')

print('\n***Ejercicio 3 - ¿Solución 2?***')
print(
    f'La fecha de hoy es: {dt.datetime.now()} y eso representa {dt.datetime.now().strftime("%f")} milisegundos')

print('\n***Ejercicio 3 - Solución 3***')
ct = dt.datetime.now().time()
td = dt.timedelta(hours=ct.hour, minutes=ct.minute,
                  seconds=ct.second, microseconds=ct.microsecond)
print(
    f'La hora actual es: {td} y eso equivale a: {td.total_seconds() * 1000:,.2f}')

# Escribir una función que obtenga el número de la semana a partir de una fecha. Por ejemplo: 16/06/2015 = 25
print('\n***Ejercicio 4 - Solución 1***')
print(
    f'La fecha de hoy es: {dt.datetime.now().date()} y estámos en la semana {dt.datetime.now().date().isocalendar()[1]} del año')

print('\n***Ejercicio 4 - Solución 1***')
print(
    f'La fecha de hoy es: {dt.datetime.now().date()} y estámos en la semana {dt.datetime.now().strftime("%W")} del año')

# Escribir una función que reciba como parámetro el año y semana del año (2015, 50) y muestre la fecha que
# corresponde al lunes de esa semana. Por ejemplo, 2015, 50 = Lunes 14 de diciembre de 2015
print('\n***Ejercicio 5 - Solución 1***')
print(
    f"La fecha del lunes de la semana 50 del año 2015 es: {dt.datetime.strptime('2015 50 1', '%Y %W %w').strftime('%A %d de %B de %Y')}")
print(
    f"La fecha del lunes de la semana 39 del año 2022 es: {dt.datetime.strptime('2022 39 1', '%Y %W %w').strftime('%A %d de %B de %Y')}")

# Escribir una función que muestre todos los domingos de un año dado
print('\n***Ejercicio 6 - Solución 1***')


def all_sundays(year):
    dtime = dt.date(year, 1, 1)  # 1 de enero del año proporcionado
    dtime += dt.timedelta(days=6 - dtime.weekday())  # Primer domingo del año
    while dtime.year == year:
        #El yield es como un return solo que lo hace en medio la ejecución. Es decir no se espera a terminar el ciclo para regresar el valor
        yield dtime
        dtime += dt.timedelta(days=7)

print('Todos los domingos del año 2020 son: ')
for s in all_sundays(2020):
    print(s.strftime("%A %d de %B de %Y"))

print('\n\nTodos los domingos del año 2022 son: ')
for s in all_sundays(2022):
    print(s.strftime("%A %d de %B de %Y"))

# Escribir una función que detenga la ejecución del código por la cantidad en segundos que recibió por parámetro
print('\n***Ejercicio 7 - Solución 1***')
sec = int(input("Por favor ingrese la cantidad de segundos a detener:\n"))
print(f"Inicia la espera de {sec} segundos...")
time.sleep(sec)
print("Finaliza la espera")

# Escriba un programa que asigne y/o actualice la zona horaria predeterminada
os.system('pip install pytz')
import pytz
print('\n***Ejercicio 8 - Solución 1***')
print("Timezones disponibles")
for timeZone in pytz.all_timezones:
    print(timeZone)

tz = pytz.timezone("America/Los_Angeles")
print(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(dt.datetime.now(tz=tz).strftime('%Y-%m-%d %H:%M:%S'))
print(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
os.system('pip uninstall pytz')

# Escriba una función que reciba como parámetro dos fechas y muestre todas las fechas entre las dos fechas proporcionadas
print('\n***Ejercicio 9 - Solución 1***')

def daterange(date1, date2):
    for n in range(int((date2 - date1).days)+1):
        yield date1 + dt.timedelta(n)

for item in daterange(dt.datetime.now().date(), dt.datetime.now().date() + dt.timedelta(days=5)):
    print(item.strftime("%d-%m-%Y"))

# Escribir un progama que muestre el segundo sábado de cada mes para un año proporcionado
print('\n***Ejercicio 10 - Solución 1***')
for month in range(1, 13):
    cal = calendar.monthcalendar(2022, month)
    first_week  = cal[0]
    second_week = cal[1]
    third_week  = cal[2]

    # Sí un Sábado se presenta en la primera semana el segundo sábado se encuentra en la segunda semana
    # sino el segundo sábado debe estar en la tercera semana
    print(calendar.SATURDAY)
    if first_week[calendar.SATURDAY]:
        holi_day = second_week[calendar.SATURDAY]
    else:
        holi_day = third_week[calendar.SATURDAY]

    print('%3s: %2s' % (calendar.month_abbr[month], holi_day))