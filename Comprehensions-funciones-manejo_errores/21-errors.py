
# print(0/0)  # Esto generará un ZeroDivisionError

#print("Este mensaje no se imprimirá debido al error anterior.")

suma = lambda x, y: x + y
assert suma(2, 2) == 4

print("Hola 1")

age = 10
if age < 18:
    raise Exception("No se permite menorres de edad")

print("Hola 2") # Este mensaje no se imprimirá debido a la excepción anterior.