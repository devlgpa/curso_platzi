
# operadores aritmeticos

x = 5
y = 10

print("Operadores Aritmeticos de", x, "y", y)

# suma
print("Suma", x + y)  # output: 15

# Resta
print("Resta", x - y)  # output: -5

# Multiplicacion  *
print("Multiplicacion", x * y)  # output: 50

# Division  /
print("Division", x / y)  # output: 0.5


# Modulo devuelve el resto al dividir  % 
print("Modulo", x % y)  # output: 5

# Potencia  **
print("Potencia", x ** 2)  # output: 25

# Division entera descarta la parte decimal //
print("Division entera", x // y)  # output: 0

numpar = 8
print("Es par?", numpar % 2 == 0)  # output: True
# % da el resto de dividir si no hay resto entonces si es par

# Precedencia de operadores

# Primero dentro de parentesis
# Luego potencias
# Luego multiplicacion, division, divisiones enteras y restos
# Suma y restas
# Comparaciones de indentidad, igualdad y pertenencia
# Logicos 