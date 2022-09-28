import os
import datetime as dt
from sys import platform
import locale

os.system('cls')

#Con dir() puede ver todas las propiedades de un objeto en python
print("***Comando 1***")
print(dir(dt))
print("**********************************++")
print(dir(dt.datetime))
print("***Comando 2***")
print(f"\n\nEl año máximo en Python es: {dt.MAXYEAR}")
print("***Comando 3***")
print(f"\n\nEl año mínimo en Python es: {dt.MINYEAR}")

print("\n\n***Comando 4***")
#Para imprimir la fecha y hora actual utilice datetime.now
print(dt.datetime.now())

print("\n\n***Comando 4***")
currentDateTime = dt.datetime.now()
#currentDateTime = dt.datetime.today()
print(currentDateTime)
print(f'Año: {currentDateTime.year}')
print(f'Mes: {currentDateTime.month}')
print(f'Día: {currentDateTime.day}')
print(f'Hora: {currentDateTime.hour}')
print(f'Minuto: {currentDateTime.minute}')
print(f'Segundo: {currentDateTime.second}')
print(f'Microsegundo: {currentDateTime.microsecond}')
print(f'Solo fecha: {currentDateTime.date()}')
print(f'Solo hora: {currentDateTime.time()}')
print(f'Día de la semana: {currentDateTime.weekday()}')#0:Lunes, 1:Martes, 2:Miércoles, 3:Jueves, 4:Viernes, 5:Sábado, 6:Domingo
print(f'today = now: {currentDateTime.today()}')

print("\n\n***Comando 5***")
currentDateTime = dt.datetime.now()
print(currentDateTime)
#Con replace, puede cambiar el valor individual de la fecha y/o de la hora, considera que no modifica la variable actual,
# sino que regresa un nuevo datetime con los nuevos valores
currentDateTime = currentDateTime.replace(minute=0,second=0,microsecond=0)
print(currentDateTime)
#Para obtener la diferencia entre horas, basta con realizar una resta. Esto regresará un objeto de tipo timedelta
elapsedTime = dt.datetime.now() - currentDateTime
print(elapsedTime)
print(type(elapsedTime))

print("\n\n***Comando 6***")
print(f'Días: {elapsedTime.days}')
print(f'Minutos: {elapsedTime.seconds/60}')
print(f'Segundos con microsegundos: {elapsedTime.total_seconds()}')
print(f'Segundos: {elapsedTime.seconds}')
print(f'Microsegundos: {elapsedTime.microseconds}')
print(f'{elapsedTime}')

print("\n\n***Comando 7***")
futureDate = dt.datetime.now() + dt.timedelta(days=5)#Agrega 5 días a la fecha actual
print(dt.datetime.now())
print(futureDate)
print('\n\nMenos 5 días')
futureDate = dt.datetime.now() + dt.timedelta(days=-5)#Resta 5 días a la fecha actual
print(dt.datetime.now())
print(futureDate)
print('\n\nMenos 5 días_2')
futureDate = dt.datetime.now() - dt.timedelta(days=5)#Resta 5 días a la fecha actual
print(dt.datetime.now())
print(futureDate)
print('\n\nMás días, horas y minutos')
futureDate = dt.datetime.now() + dt.timedelta(days=5,hours=2,minutes=20)
print(dt.datetime.now())
print(futureDate)

print("\n\n***Comando 8***")
print(dt.time())#dt.time inicializa el tiempo en 00:00:00
currentDate = dt.datetime.now().combine(dt.datetime.today(), dt.time())
print(currentDate)

print("Specific date")
print(dt.time(hour=18,minute=32,second=30))
print(dt.date(year=2022, month=1, day=1))
print(dt.datetime.combine(dt.date(year=2022, month=1, day=1), dt.time(hour=18,minute=32,second=30)))
print(dt.datetime(year=2022, month=1, day=1, hour=18,minute=32,second=30))

print('Formato de fecha')
currentDate = dt.datetime.now()
print(currentDate.strftime("%B %d, %Y"))
print(currentDate.strftime("%B %d, %Y - %H:%M"))
#Puedes validar los diferentes formatos en la siguiente liga: https://strftime.org/

print("Fecha a partir de una cadena")
print(dt.datetime.strptime("26/03/2022", "%d/%m/%Y"))
print(dt.datetime.strptime("26/03/2022 18:00:00", "%d/%m/%Y %H:%M:%S"))

print("\n\n***Comando 8***")
centralTime = dt.timezone(dt.timedelta(hours=-5))
print("Central Time -5")
print(centralTime)
pacificTime = dt.timezone(dt.timedelta(hours=-8))
print("Pacific Time -8")
print(pacificTime)
easternTime = dt.timezone(dt.timedelta(hours=-4))
print("Eastern Time -4")
print(easternTime)

print("\n\nAplicar Zona Horaria")
print("Central Time -5")
print(dt.datetime.now(centralTime));#La zona horaria solo aplica con datetime.now, no puede aplicar con datetime.today
print("Pacific Time -8")
print(dt.datetime.now(pacificTime));
print("Eastern Time -4")
print(dt.datetime.now(easternTime));
print("Aplicar otra zona horaria a un datetime con zona horaria definida")
print(dt.datetime.now(centralTime).astimezone(pacificTime));


print("\n\nLocale")
if platform == 'win32':
    locale.setlocale(locale.LC_ALL, 'en_US')
else:
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

date_time = dt.datetime(2022, 1, 15, 20, 40, 50)

print("#####English US#####")
print("Date: " + date_time.strftime("%B-%d-%Y"))
print("Time: " + date_time.strftime("%X"))
print("Weekday: " + date_time.strftime("%A"))

if platform == 'win32':
    locale.setlocale(locale.LC_ALL, 'de_DE')
else:
    locale.setlocale(locale.LC_ALL, 'de_DE.ISO8859-1')

print("#####German#####")
print("Date: " + date_time.strftime("%B-%d-%Y"))
print("Time: " + date_time.strftime("%X"))
print("Weekday: " + date_time.strftime("%A"))

if platform == 'win32':
    locale.setlocale(locale.LC_ALL, 'es_MX')
else:
    locale.setlocale(locale.LC_ALL, 'es_MX.ISO8859-1')

print("#####Español#####")
print("Date: " + date_time.strftime("%B-%d-%Y"))
print("Time: " + date_time.strftime("%X"))
print("Weekday: " + date_time.strftime("%A"))