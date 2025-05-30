
#kwargs es para trabajar con argumentos con etiquetas es decir llave y valor (diccionarios)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print ("  ")

# Llamada a la función con diferentes argumentos
print_info(name = "Carlos", age = 30, city = "Bogotá")
print_info(name = "Carlos", age = 30, city = "Bogotá", country = "Colombia")
#llaves: name, age, city, country