numbers = {1:"uno", 2:"dos", 3:"tres"}   #este es un diccionario
print (numbers)

information = {"nombre": "Chalo",
               "Apellido": "Palacios",
               "Edad": "19"}
print (information)
del information["Edad"]
print (information)

claves = information.keys()
print (claves)
print (type(claves))
values = information.values()
print (values)
pairs = information.items()
print(pairs)

contacts = {"Chalo":{"Apellido": "Palacios",
                     "Pais": "Peru",
               "Edad": "19"},
            "Luis":{"Apellido": "Palacio",
                    "Pais": "Persia",
               "Edad": "99"}}
print (contacts)
print (contacts["Chalo"])