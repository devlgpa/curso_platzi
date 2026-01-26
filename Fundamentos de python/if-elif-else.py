
x = 5
y = 4
z = 14

if x > y or x > z:
    print("x es mayor que y o que z")
elif x == y:
    print("x es igual a y")
else:
    print("Ninguna de las condiciones anteriores se cumple")

a = "Python"
b = "Javascript"
c = "Python"

if a == c:
    if a != b:
        print("a es igual a c y diferente de b")
    else:
        print("estor saliendo por el else del if interno")
else:
    print("a no es igual a c")

e = 10
f = 10

if e == f:
    # No se que hacer si estas dos variables son iguales
    pass #Para ignorar la estructura if hasta que definamos el código a ejecutar