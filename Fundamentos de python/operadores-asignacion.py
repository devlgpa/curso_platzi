
# Operadores de asignación

x = 5
#x = x + 3  # asigna a x el valor de x + 3

x += 3  # equivalente a x = x + 3
x -= 3  # resta
x *= 3  # multiplicacion
x /= 3  # division nos dara un float
x %= 2  # modulo(resto)

y = 20

y //= 3  # division entera ignora la parte decimal
y **= 2  # potencia 20 * 20 

# WALRUS OPERATOR (operador morsa) :=

print(z := 10)  # asigna 10 a z y lo imprime
print(z)