from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import registro_form, inicio_form
from django.contrib.auth.decorators import login_required
from .models import Producto, Carrito, ItemCarrito


# Create your views here.


def base(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.itemcarrito_set.all()
    items_carrito = sum(item.cantidad for item in items)

    return render(request, "base.html", {"items_carrito": items_carrito})


def index(request):
    productos = (
        Producto.objects.all()
    )  # Recupera todos los productos de la base de datos
    return render(request, "index.html", {"productos": productos})


def carrito(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.itemcarrito_set.all()
    cantidad_items = sum(item.cantidad for item in items)

    precio_total = sum(item.producto.precio * item.cantidad for item in items)

    if request.method == "POST":
        item_id = request.POST.get("item_id")
        try:
            item = ItemCarrito.objects.get(id=item_id)
            item.delete()
        except ItemCarrito.DoesNotExist:
            print("El item no existe en el carrito.")
        return redirect("carrito")

    return render(
        request,
        "carrito.html",
        {
            "items": items,
            "carrito": carrito,
            "cantidad_items": cantidad_items,
            "precio_total": precio_total,
        },
    )


def compra(request):
    return render(request, "compra.html")


def user(request):
    return render(request, "user.html")


@login_required
def producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)

    if request.method == "POST":
        carrito, creado = Carrito.objects.get_or_create(usuario=request.user)

        item_carrito, creado = ItemCarrito.objects.get_or_create(
            carrito=carrito, producto=producto
        )
        item_carrito.cantidad += 1
        item_carrito.save()
        return redirect("producto", producto_id=producto_id)

    return render(request, "producto.html", {"producto": producto})


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
