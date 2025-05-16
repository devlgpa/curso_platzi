
from enum import Enum

class OrderStatus(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3

def verificar_estado_orden(status):
    if status == OrderStatus.PENDIENTE:
        return "La orden está pendiente."
    elif status == OrderStatus.ENVIADO:
        return "La orden ha sido enviada."
    elif status == OrderStatus.ENTREGADO:
        return "La orden ha sido entregada."

estado_1 = OrderStatus.ENVIADO
estado_2 = OrderStatus.ENTREGADO
estado_3 = OrderStatus.PENDIENTE

print(verificar_estado_orden(estado_1))  # Output: La orden ha sido enviada.
print(verificar_estado_orden(estado_2))
print(verificar_estado_orden(estado_3))
