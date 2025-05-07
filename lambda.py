add = lambda a, b: a + b
print (add(10,4))

multiply = lambda a, b: a * b
print (multiply(80,5))

#cuadrado de cada numero
numbers = range(11)     #range genera 11 numeros contando el cero
squared_numbers = list(map(lambda x : x**2, numbers))       #esto nos generara un lista con una funcion map que dentro se potencien
print ("Cuadrados: ", squared_numbers)

#Pares
even_numbers = list(filter(lambda x: x%2 == 0, numbers))  #aqui filter filtrara los elemento que cumplan con la condicion
print ("Pares: ", even_numbers)