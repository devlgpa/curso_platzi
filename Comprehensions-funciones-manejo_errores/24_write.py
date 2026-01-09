
# r -> read
# w -> write (si el archivo no existe lo crea, si existe borra todo su contenido)
# r+ -> read and write (no borra el contenido del archivo)
# w+ -> write and read (si el archivo no existe lo crea, si existe borra todo su contenido)
with open("./Comprehensions-funciones-manejo_errores/text.txt", "w+") as file:
    for linea in file:
        print(linea)
    file.write("Nueva linea agregada\n")
    file.write("Otra linea agregada\n")
    file.write("mas lineas\n")