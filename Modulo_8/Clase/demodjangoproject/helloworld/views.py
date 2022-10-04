from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django import http
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

def greetings(request):
    return HttpResponse("Hola, bienvenido a Django")

#recuerda comentar la línea 'django.middleware.csrf.CsrfViewMiddleware' de settings.py que no sirve pa na
def execute_post(request):
    if request.method == 'POST':
        return HttpResponse("Hola, bienvenido a Django desde POST")
    elif request.method == 'GET':
        return HttpResponse("Hola, bienvenido a Django desde GET")

def execute_put(request):
    if request.method == 'PUT':
        return HttpResponse("Hola, bienvenido a Django desde PUT")
    elif request.method == 'GET':
        return HttpResponse("Hola, bienvenido a Django desde GET")

def execute_delete(request):
    if request.method == 'DELETE':
        return HttpResponse("Hola, bienvenido a Django desde DELETE")
    
    return HttpResponseNotAllowed(permitted_methods=['DELETE'])

def greetings_message(request, message):
    if request.method == 'GET':
        return HttpResponse(f"El mensaje es: {message}")
    
    return HttpResponseNotAllowed(permitted_methods=['DELETE'])

def greetings_age(request, age:int):
    if request.method == 'GET':
        return HttpResponse(f"Tienes {age} años")
    
    return HttpResponseNotAllowed(permitted_methods=['DELETE'])

def greetings_query_string(request):
    if request.method == 'GET':
        return HttpResponse(f"Valor del parámetro: {request.GET.get('name')} - {request.GET.get('lastName')}")
    
    return HttpResponseNotAllowed(permitted_methods=['DELETE'])

def index_html(request):
    if request.method == 'GET':
        template = loader.get_template('index.html')
        context = {
            'html_title':'Mi primera aplicación con Django',
            'html_user':'Abraham'
        }
        return HttpResponse(template.render(context, request))
    
    return HttpResponseNotAllowed(permitted_methods=['GET'])

#Ejecuta esta línea de código si quieres saber que clases forman al módulo http
#print(dir(http))