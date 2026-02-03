
# Tupla : coleccion de ordenada e inmutable de elementos

# indice :        0         1           2          3
tecnologias = ("python", "javasript", "go", "python")

print (tecnologias)
print (tecnologias[1])

print (len(tecnologias))

print (type(tecnologias))

fruta = ("manzana",)

print (type(fruta))

tupla = ("python", 5 , True)

print (tupla)
print (type(tupla))

x, y, z = tupla
print (x)
print (y)
print (z)

tupla1 = (1, 2, 3)
tupla2 = (3, 4, 5, 6)
tupla3 = tupla1 + tupla2
print (tupla3)

tupla = ("python", 5 , True)

print (tupla * 2)

for item in tupla:
    print (item)

print ("-----------------------------------")

tuplaAmodificar = ("python", "javascript", "go")
listaComodin = list(tuplaAmodificar)
print (listaComodin)
listaComodin.append("ruby")
print (listaComodin)
tuplaModificada = tuple(listaComodin)

print (tuplaModificada)