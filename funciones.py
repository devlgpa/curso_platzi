def greet(name, last_name = "no tiene apellido"):#en el caso de que no ponga apellido elvalor por defecto sera el que esta en ""
    print ("hola ", name, last_name)

greet("Chalo", "palacio")
greet("luis")
greet(last_name="palacios", name="Chalo") #podemos espedificar el valor que qeramos sin importar el orden al poner