from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, "index.html")


def ingresar(request):
    return render(request, "aut/ingresar.html")


def registrar(request):
    return render(request, "aut/registrar.html")


def cerrar_sesion(request):
    return redirect("index")
