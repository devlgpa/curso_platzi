to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar el museo",
         "Volver al hotel"]

print (to_do)

numbers = [1, 2, 3, "cinco"]

print (numbers)
print (type(numbers))

mix = ["uno", 2 , 3, 14.23, True, [1, 2, 3]]

print (mix)
print (len(mix))

print ("Primer elemento: ", mix[0])
print ("Segundo elemento: ", mix[1])
print ("Ultimo elemento: ", mix[-1])

string = "Hola mundo"

print ("Primer elemento", string[0])
print ("Segundo elemento", string[1])
print ("Ultimo elemento", string[-1])

print (mix[1:])   #del primer elemento al ultimo
print (mix)

mix.append(False)  #le agregamos al final el booleano false
print (mix)
mix.append([5, 7])
print (mix)

mix.insert(1, ["a", "b"])   #insertamos en la segunda posiocion que es 1 donde esta el 2 y le ponemos a, b mas no lo eliminamos el que estaba ahi
print (mix)

numbers = [1, 2, 100, 0, 90.45]
print (numbers)
print ("Mayor: ", max(numbers))
print ("Menor: ", min(numbers))
del numbers[-1]    #del eliminara el numero que este en la posicion entre los []
print (numbers)
del numbers[:2]
print (numbers)
del numbers    #este elimina toda la lista numers
print (numbers)