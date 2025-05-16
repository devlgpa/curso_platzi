# Con Chatgpt y algo de intervencion

from collections import deque, Counter, defaultdict
from enum import Enum
import random

# Enum para estado de la orden
class EstadoOrden(Enum):
    PENDIENTE = "Pendiente"
    PROCESADA = "Procesada"
    CANCELADA = "Cancelada"


# Clase para una orden
class Orden:
    def __init__(self, cliente, producto, cantidad):
        self.id = random.randint(1000, 9999)
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
        self.estado = EstadoOrden.PENDIENTE

    def __str__(self):
        return f"Orden #{self.id} | Cliente: {self.cliente} | Producto: {self.producto} x{self.cantidad} | Estado: {self.estado.value}"

# Tiendita
class Tienda:
    def __init__(self):
        self.inventario = defaultdict(int)
        self.ordenes = deque()
        self.ventas = Counter()

    def agregar_producto(self, producto, cantidad):
        self.inventario[producto] += cantidad
        print(f"Se agregaron {cantidad} unidades de {producto} al inventario.")

    def realizar_orden(self, cliente, producto, cantidad):
        orden = Orden(cliente, producto, cantidad)
        if self.inventario[producto] >= cantidad:
            self.inventario[producto] -= cantidad
            orden.estado = EstadoOrden.PROCESADA
            self.ventas[producto] += cantidad
            print(f"\n✅ Orden realizada: {orden}")
        else:
            orden.estado = EstadoOrden.CANCELADA
            print(f"\n❌ No hay suficiente o no se tiene {producto} en inventario.")
        
        self.ordenes.append(orden)

    def verificar_ordenes(self):
        print("\n\033[1m📋 Estado de órdenes:\033[0m")
        for orden in self.ordenes:
            print(orden)

    def ver_inventario(self):
        print("\n\033[1m📦 Inventario actual:\033[0m")
        for producto, cantidad in self.inventario.items():
            print(f"- {producto}: {cantidad} unidades")

    def ver_ventas(self):
        print("\n\033[1m💰 Ventas realizadas:\033[0m")
        if not self.ventas:
            print("📭 No se ha vendido nada aún.")
        else:
            for producto, cantidad in self.ventas.items():
                print(f"- {producto}: {cantidad} unidades vendidas")
        print("\n")


# -----------------------
# Uso de ejemplo
# -----------------------

tienda = Tienda()

# Agregar productos
tienda.agregar_producto("Manzanas", 10)
tienda.agregar_producto("Pan", 5)

# Realizar órdenes
"""tienda.realizar_orden("Ana", "Manzanas", 4)
tienda.realizar_orden("Luis", "Pan", 2)
tienda.realizar_orden("Pedro", "Pan", 4)  # Esto puede fallar si no hay suficiente"""

tienda.ver_inventario()

name = str(input("\nIngrese su nombre: "))
product = str(input("Que producto desea comprar: "))
cant = int(input("cuantos desea comprar: "))

tienda.realizar_orden(name, product, cant)

# Revisar todo
tienda.verificar_ordenes()
tienda.ver_inventario()
tienda.ver_ventas()
