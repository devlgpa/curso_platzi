#iteradores para los numeros impares

#limite
limit = 10

odd_itter = iter (range(1, limit+1, 2))           #range(start, stop, step)  el comiento, cuando se acaba y el rango al que avanza

#usar el iterador
for num in odd_itter:         #para cada num en el odd_iterr lo imprimira
    print (num)

