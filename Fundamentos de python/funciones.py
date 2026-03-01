
# Funcion: es un bloque de codigo que solo se ejecuta cuando lo llamamos

def saludar(nombre, nacionalidad = "nacionalidad por defecto"):  # Argumentos
    print ("Hola", nombre, nacionalidad)

saludar("Alice", "España") # Parametros
saludar("Bob", "Peru")
saludar("Charlie") # Usando el valor por defecto para el apellido

def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado)

def funcion():
    pass         # pass se utiliza para indicar que no se ha implementado el cuerpo de la función aún, pero se quiere evitar un error de sintaxis.
