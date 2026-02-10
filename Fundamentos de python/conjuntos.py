
# Conjunto (set): coleccion no ordenada de elementos unicos (no se puede acceder por inidice)

frutas = {"manzana", "banana", "cereza", "manzana"}

print (frutas)
print (type(frutas))
print (len(frutas))

print ("banana" in frutas)
print ("pera" in frutas)

#agregar
#add

frutas.add("pera")
print (frutas)

# update : agregar varios elementos

frutasTropicales = ["kiwi", "mango", "uva"]

frutas.update(frutasTropicales)
print (frutas)

# eliminarlos

# remove y discard
frutas.remove("banana")
print (frutas)
frutas.discard("cereza")
print (frutas)

# pop : elimina un elemento aleatorio
frutaEliminada = frutas.pop()
print (f"La fruta eliminada fue: {frutaEliminada}")
print (frutas)

# clear : vacia el conjunto
frutas.clear()
print (frutas)

"""conjuntos = {"python", 167, True}

print (conjuntos)
print (type(conjuntos))

for item in conjuntos:
    print (item)"""

print ("-----------------------------------")

conjuntoA = {"a", "c", "f"}
conjuntoB = {"b",  "c", "g"}

# union de conjuntos todos los elementos juntos
c = conjuntoA.union(conjuntoB)
print (c)

# interseccion elementos que estan en ambos
i = conjuntoA.intersection(conjuntoB)
print (i)

# diferencia elementos que estan en grupo a pero no en b
d = conjuntoA.difference(conjuntoB)