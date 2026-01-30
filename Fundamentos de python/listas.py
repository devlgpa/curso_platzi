
# LISTAS : las listas son ordenadas, modificables y permiten valores duplicados

#indices :    0          1           2           3
"""frutas = ["Manzana", "Naranja", "Mandarina", "Naranja"]
print (frutas)
print (type(frutas))

frutas[1] = "Banana"

print (frutas[1])
print (frutas)

lista = ["Sergio code", 5, True]
print (lista)
print (type(lista))

print (len(lista))
print (len(frutas))

print(frutas[1:])  # si no hay valor despues/antes de : va hasta el final/inicio
if "Manzana" in frutas:
    print ("La Manzana esta dentro de frutas")
"""
# Indice :     0       1        2
vehiculos = ["Auto", "Moto", "Avion"]

# Metodos

# Append : agregar un elemento al final de la lista
vehiculos.append("Barco")
print (vehiculos)

# Insert
vehiculos.insert(1, "Bicicleta")
print (vehiculos)

# Remove
vehiculos.remove("Auto")
print (vehiculos)

# Pop
vehiculos.pop(1)
print (vehiculos)

# Sort : se ordena alfabeticamente
vehiculos.sort()
print (vehiculos)

# Reverse : lo contrario de sort
vehiculos.reverse()
print (vehiculos)

# Unir listas
coleccion_1 = [1, 2, 3]
coleccion_2 = [4, 5, 6]

coleccion_3 = coleccion_1 + coleccion_2
print (coleccion_3)

coleccion_1.extend(coleccion_2)
print (coleccion_1)
