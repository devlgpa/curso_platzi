#el ./ abre el archivo desde la ruta de la terminal mas no desde la ruta del archivo .py
#file = open("./text.txt", "r")

file = open("./Comprehensions-funciones-manejo_errores/text.txt", "r")

#lee todo el archivo
#print(file.read())

#lee linea por linea
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())

#lee todas las lineas y las guarda en una lista
#for line in file:
#    print(line)

#cerrar el archivo  
#file.close()

#otra forma de abrir archivos (recomendada) ya que una vez que se sale del bloque with, el archivo se cierra automaticamente
with open("./Comprehensions-funciones-manejo_errores/text.txt", "r") as file:
    for line in file:
        print(line)