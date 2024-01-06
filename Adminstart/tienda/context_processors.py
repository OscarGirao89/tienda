from .models import Carrito
from django.db.models import Sum


def items_carrito(request):
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    items_carrito = (
        carrito.itemcarrito_set.aggregate(total_items=Sum("cantidad"))["total_items"]
        or 0
    )

    return {"items_carrito": items_carrito}
