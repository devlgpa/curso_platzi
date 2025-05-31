
#esto nos ayudara a limpiar la terminal
import os 

# Lista global para guardar los productos
productos = []
carrito = []

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_total(*precios, **opciones):
    total = sum(precios)
    descuento = opciones.get("descuento", 0)
    if descuento:
        total -= total * (descuento/100)
    return total

# Listas globales
productos = []
carrito = []

def add_product(nombre, precio):
    productos.append({"nombre": nombre, "precio": int(precio)})

def mostrar_tabla_lado_a_lado():
    max_filas = max(len(productos), len(carrito))

    print(f"{'Productos':<15} {'Precio':>8}       {'Carrito':<15} {'Precio':>8}")
    print("-" * 25 + "      " + "-" * 25)

    for i in range(max_filas):
        # Columna de productos
        if i < len(productos):
            prod_nombre = productos[i]['nombre']
            prod_precio = f"{productos[i]['precio']:.2f}"
        else:
            prod_nombre = ""
            prod_precio = ""

        # Columna del carrito
        if i < len(carrito):
            cart_nombre = carrito[i]['nombre']
            cart_precio = f"{carrito[i]['precio']:.2f}"
        else:
            cart_nombre = ""
            cart_precio = ""

        print(f"{prod_nombre:<15} {prod_precio:>8}       {cart_nombre:<15} {cart_precio:>8}")

    # Mostrar total del carrito
    total = sum(p['precio'] for p in carrito)
    print("-" * 25 + "      " + "-" * 25)
    print(f"{'':<25}      {'TOTAL':<15} {total:>8.2f}")

# Agregar productos
add_product("platano", 9)
add_product("manzana", 8)
add_product("naranja", 12)
add_product("mango", 10)
add_product("coco", 16)
add_product("tomate", 6)


# Bucle principal
while True:
    limpiar_pantalla()
    mostrar_tabla_lado_a_lado()

    eleccion = input("\nEscribe el nombre del producto que quieres comprar (o 'salir' para terminar): ").strip()

    if eleccion.lower() == "salir":
        break

    encontrado = next((p for p in productos if p["nombre"].lower() == eleccion.lower()), None)

    if encontrado:
        carrito.append(encontrado)
        print(f"\n✅ '{encontrado['nombre']}' agregado al carrito.")
    else:
        print("\n❌ Producto no encontrado. Intenta de nuevo.")

    input("\nPresiona Enter para continuar...")

descuentos = input("\n¿Cuenta con algún descuento? (sí/no): ").strip().lower()
if descuentos == "si" or descuentos == "sí":
    descuent = int(input("¿De cuánto es el descuento (%): "))
    precios_enteros = [int(item["precio"]) for item in carrito]
    total_original = sum(precios_enteros)
    #el * desempaquetara la lista ya que args no acepta listas solo argumentos
    total_con_descuento = calcular_total(*precios_enteros, descuento=descuent)
    
    print(f"\nTotal a pagar: ${total_original:.2f}")
    print(f"Descuento del {descuent}%")
    print(f"Total con descuento: ${total_con_descuento:.2f}")
else:
    total = sum(p["precio"] for p in carrito)
    print(f"\n💰 Total a pagar: ${total:.2f}")



