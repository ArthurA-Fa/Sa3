from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def func1(request):
    return render(request, "app_aula/home.html")

def func2(request):
    return render(request, "app_aula\extra.html")

def func3(request):
    return render(request, "app_aula\informacoes.html")
