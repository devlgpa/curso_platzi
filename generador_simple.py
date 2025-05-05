def my_generator():   #funcion mi generador generara el 1, 2, 3
    yield 1
    yield 2
    yield 3

for value in my_generator():    #Para cada valor que genero mi generador lo imprimira
    print (value)