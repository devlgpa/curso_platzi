a = [1, 2, 3, 4, 5]
b = a

print (a)
print (b)
del a[0]   #eliminamos el primer elemento de la lista

print (id(a))
print (id(b))

c = a[:]   # el c copiara todo lo que hay de la lista a dela posicion 0 al final que es solo poninendo los :
print (id(a))
print (id(b))
print (id(c))

a.append(6)  #agregamos al final el valor 6
print (a)
print (b)
print (c)