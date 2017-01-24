from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango, stay away from me. \n I mean it.")
