#Fibonacci
#0 1 1 2 3 5 8 13 21

def fibonacci(limit):
    a, b = 0, 1           #dos valores iguales a 2   aqui el a sera igual a 0 y el b igual a 1 se separan por las comas
    while a < limit:      
        yield a            #mientras el a sea menor al limite la generara 
        a, b = b, a + b      #aqui el a tomara el valor de b y el b tomara el valor de a + b

for num in fibonacci(10):
    print (num)