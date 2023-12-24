from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Hola Django 2")

def xd(request):
    return render(request, 'xd.html')