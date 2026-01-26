
# Operadores de comparación

x = 5
y = 3
z = 5

print(x == y)  # si son iguales: True sino False
print(x != y)  # si son diferentes: True sino False
print(x > y)   # Es mayor que la segunda: True
print(x < y)   # Es menor que la segunda: False
print(x >= z)  # mayor o igual: True
print(x <= z)  # menor o igual: True

# Operadores lógicos

print(x > y and y > z)  # ambas condiciones deben ser True para devolver True

print(x > y or y > z)   # al menos una condición debe ser True para devolver True

v = True
print("invertimos el valor de v:", v,"a", not v)  # invierte el valor: False