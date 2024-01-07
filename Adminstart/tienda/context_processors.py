from .models import Carrito
from django.db.models import Sum


def items_carrito(request):
    carrito = None
    creado = False

    if request.user.is_authenticated:
        carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    total_items_carrito = (
        carrito.itemcarrito_set.aggregate(Sum("cantidad"))["cantidad__sum"]
        if carrito
        else 0
    )

    return {
        "items_carrito": carrito.itemcarrito_set.all() if carrito else [],
        "carrito": carrito,
        "creado": creado,
        "total_items_carrito": total_items_carrito,
    }
