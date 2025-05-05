#ejemplo de iterador

#crear una lista
my_list = [1, 2, 3, 4]

#obtener el iterador
my_iter = iter(my_list)

#usar el iterador
print (next(my_iter))         #next no permite ver los velores que se van guardando en memoria
print (next(my_iter))      #imprimira el siguiente elemento
print (next(my_iter))   
print (next(my_iter))      