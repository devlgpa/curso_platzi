

print('Hola "mundo"') # uso de comillas dobles dentro de comillas simples
print("Hola 'mundo'") # uso de comillas simples dentro de comillas dobles

ingles = "I am Luis"

multiples = """Hola
mundo"""
print(ingles)
print(multiples)

palabra = "murcielago"
print(len(palabra))  # output: 10 las letras de la palabra murcielago

texto = "Este curso es de fundamentos de python"

estaIncluido = "python" in texto  # output: True
noEstaIncluido = "java" not in texto  # output: True

print(estaIncluido)
print(noEstaIncluido)

mayusculas = texto.upper()  # convierte a mayusculas
minusculas = texto.lower()  # convierte a minusculas
print(minusculas)
print(mayusculas)

texto2 = texto.upper()
texto2 = texto.lower()
print(texto2) 

espacios = "          Hola mundo         "
sinEspacios = espacios.strip()  # elimina los espacios en blanco al inicio y al final muy util para contraseñas con espacios extras
print(espacios)
print(sinEspacios)