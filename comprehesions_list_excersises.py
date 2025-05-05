#dobles de unos numeros con lista compresa

numeros = [1, 2, 3, 4, 5, 6]
doble_num = [x * 2 for x in numeros]
print ("Dobles: ", doble_num)

#filtrar y transformar

palabras = ["sol", "mar", "montaña", "rio", "estrella"]
filtro = [palabra.upper() for palabra in palabras if len(palabra) > 3]
print ("Palabras filtradas en mayusculas: ", filtro)

#crear un diccionario con list comprehesion

claves = ["nombre", "edad", "ocupacion"]
valores = ["Juan", "30", "Ingeniero"]

diccionario = {claves[i]:valores[i] for i in range(len(claves))}
print ("Diccionario creado: ", diccionario)

#anidacion de una list comprehesions

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
transpuesta_comprehension = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print("Transpuesta con List Comprehension:", transpuesta_comprehension)

#extraer informacion de un lista de diccionarios

personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]
nombres_madrid = [persona["nombre"] for persona in personas if persona["ciudad"] == "Madrid" and persona["edad"] > 30]
print("Nombres de personas en Madrid mayores de 30 años:", nombres_madrid)