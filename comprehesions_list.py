#la ventaja que trae es que no ocupan mucho espacio como imprimir un por 1 
squares = [x ** 2 for x in range(1,11)]      #lista comprimida elevara al cuadrado para cada x en un rango del 1 al 11

#print ("Cuadrado: ", squares)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
#print ("Temperatura en F: ", fahrenheit)

#numeros pares
evens = [x for x in range(1, 21) if x%2 == 0]    #por cada x en el rango 1 al 20, si x es para el % lo divide y da lo que sobra asi que si no sobra entonces es par
#print (evens)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print (matrix)
print (transposed)