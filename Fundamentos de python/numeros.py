
x = 1
y = 2.5
z = 1j

print(type(x))
print(type(y))
print(type(z))

positivo = 5.5
negativeo = -5.5
imaginario = -3 - 5j

xf = float(x)  # convierte un entero a flotante

print(type(xf))
print(xf)

ye = int(y)  # convierte un flotante a entero

print(type(ye))
print(ye)

# no se puede convertir un numero complejo a otro tipo de numero

entero = 5
flotante = 5.5

enteroComplejo = complex(entero)  # convierte un entero a complejo
flotanteComplejo = complex(flotante)  # convierte un flotante a complejo

print(type(enteroComplejo))
print(enteroComplejo)

print(type(flotanteComplejo))
print(flotanteComplejo)

import random

print(random.randrange(1, 10))  # output: un numero aleatorio entre 1 y 9
