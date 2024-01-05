from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import registro_form, inicio_form
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, "index.html")


def carrito(request):
    return render(request, "carrito.html")


def user(request):
    return render(request, "user.html")


def ingresar(request):
    if request.method == "POST":
        form = inicio_form(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect("index")
    else:
        form = inicio_form()

    return render(request, "aut/ingresar.html", {"form": form})


def registrar(request):
    if request.method == "POST":
        form = registro_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("ingresar")
    else:
        form = registro_form()

    return render(request, "aut/registrar.html", {"form": form})


def cerrar_sesion(request):
    logout(request)
    return redirect("index")
