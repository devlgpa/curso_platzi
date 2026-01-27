
palabra = "python"

# Recorremos cada letra en la palabra
for letra in palabra:
    print(letra)

adjetivos = ["rica", "Saludable"]
frutas = ["manzana", "platano", "pera", "naranja", "kiwi"]

for adjetivo in adjetivos:
    for fruta in frutas:
        print(fruta, adjetivo)

# Recorremos cada fruta (elemento) en la lista de frutas
"""for fruta in frutas:
    if fruta == "pera":
        continue  # Saltamos la iteración cuando la fruta es "pera"
    print(fruta)
else:
    print("Hemos terminado de recorrer el bucle for")
"""
print("---------------------------")

# Range

# Comienza desde 0 y termina en el número indicado (10), sin incluirlo
"""for i in range(10):
    print(i)
"""
"""for i in range(3, 5):
    print(i)"""

"""for i in range(0,10,2): # numero, hasta, de cuanto en cuanto
    print(i)"""


for i in range(10):
    pass