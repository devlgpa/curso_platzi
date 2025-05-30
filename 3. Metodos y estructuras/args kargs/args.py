
#args es para aceptar valores indefinidos en cantidad (tuplas)
def sum_numbers(*args):
    return sum(args)

# Llamada a la función con diferentes números de argumentos
print(sum_numbers(1, 2, 3, 4, 5))  # recibimos 5 argumentos
print(sum_numbers(1, 2))           # Recibimos 2 argumentos
print(sum_numbers(7, 8, 9, 10))    # Recibimos 4 argumentos