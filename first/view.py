from django.http import HttpResponse
from django.shortcuts import render


def saludo(request):
    return HttpResponse("Hola mundo")

def principal(request):
    return render(request, "principal.html")