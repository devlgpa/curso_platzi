#iterar en cadenas

#creando la cadena
text = "Hola mundo"

#creando el iterador
iter_text = iter(text)

#iterar en la cadena
for char in iter_text:      #para cada valor dentro del texto lo imprimira incluido el espacio
    print (char)