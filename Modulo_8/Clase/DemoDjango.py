#1. Valida que en el entorno global tengas instalado el paquete "virtualenv". Puedes hacerlo con "pip list"
#2. Si no tienes instalado el paquete "virtualenv" puedes instalar con "pip install virtualenv"
#3. Crea un entorno virtual con el nombre "demo_django" con "py -m venv demo_django". Puede ser en el path de tu elección
#4. Esto creará el dirctorio "[path seleccionado]\demo_flask". en este ejemplo:
# "C:\EduIT_Curso_Python\Modulo_8\Clase\demo_django"
#5. Selecciona el interprete correcto en VS Code apuntando al vend creado y abre una consola nueva a partir de ese interprete para que active
# el venv creado.
#6. Asegurandote que la consola de VS Code está trabajando con el ambiente creado. Instala el paquete de Django
# con "py -m pip install Django"
#7. Puedes revisar la versión de Django con el comando "django-admin --version"
#8. Asegurate de que la consola de VS Code se encuentre en el Path donde quieres que se guarden los archivos de Django
#9. Ahora debemos crear un proyecto Django con el comando: "django-admin startproject demodjangoproject" donde la palabra "demodjangoproject" indica el
#nombre del proyecto a crear. Puedes cambiar el nombre si así lo deseas
#10. El paso anterior creará una carpeta de nombre "demodjangoproject" donde podrás encontras subcarpetas y archivos.
#11. Para ejecutar el proyecto, asegurate que la consola de VS Code se encuentre dentro de la carpeta que se creó
#como parte del proyecto django, en este caso: C:\EduIT_Curso_Python\Modulo_8\Clase\demodjangoproject>
#12. Finalmente, ejecuta el comando "py manage.py runserver" para levantar la app
#13. Abre la URL que te mustra en consola para ver la aplicación web: http://127.0.0.1:8000/
#14. Hasta este punto se ha creado el cascarón para poder trabajar con django. Dicho de manera formal, lo único
#que hemos creado hasta este momento es el server de Django.
#15. Django trabaja con un esquema de "apps" es decir, si quieres agregar una página HTML debes crear un "app" lo mismo 
#si quieres crear un sistema de páginas para administrar usuarios por ejemplo. Django solo trbaja con app
#para eso ejecutamos el siguiente comando: "py manage.py startapp helloworld", donde "helloworld" es el nombre de la app
#sientete libre de cambiarlo si así lo deseas
#16. Éste último comando creará una carpeta con el mismo nombre de la app. En este caso "helloworld"
#17. En el archivo views.py agrega el siguiente código:
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello world!")
#18. Básicamente, en el archivo "views.py" contiene funciones que reciben http requests y regresan un http response,
#estas respuesta no necesariamente deben ser páginas HTML
#19. Ya que tenemos una función que recibe peticiones y regresa una respuesta hace falta enlazarla con un URL para
#que pueda ser llamada. Para eso creamos un archivo de nombre "urls.py" en el mismo nivel que el archivo "views.py"
#20. En el archivo "urls.py" agregue el siguiente bloque de código
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
#21. Por último, asegurese que el archivo "urls.py" dentro de la carpeta "demodjangoproject" agregue la URL para la app
#que acabamos de crear. El código al final del archivo de quedar algo similar a esto:
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('helloworld/', include('helloworld.urls')),
    path('admin/', admin.site.urls),
]
#
#
#
