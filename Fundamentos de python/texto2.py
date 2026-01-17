
# ind 12345
texto = "esto es un texto"

print(texto[0]) # siempre se empieza a contar desde el 0

print(texto[0:6]) # desde el indice 0 hasta el 6 sin incluir el 6 el espacio cuenta como indice

print(texto[5:]) # desde el indice 5 hasta el final

print(texto[:6]) # desde el inicio hasta el indice 6 sin incluir el 6

print(texto[:-3]) # desde el inicio hasta el indice -3 sin incluir el -3

curso = "Este curso es de Fundamentos de Python"

print( curso.replace("Python", "Java") ) # reemplaza una palabra por otra pero solo en la impresion no modifica la variable original

print(curso)

textoDividido = texto.split(" ") # divide el texto en palabras usando espacio como separador generando una lista

print(textoDividido)

#normalizacion de texto

texto2 = "Este texto tiene MAYUSCULAS y minusculas y necesito encontrar ciertas palabras"

print("mayusculas".lower() in texto2.lower()) # normaliza a minusculas para hacer la busqueda sin importar mayusculas o minusculas