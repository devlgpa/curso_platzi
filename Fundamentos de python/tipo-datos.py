
#strings o cadenas de texto

comillassimples = 'Hola, soy una cadena con comillas simples'
comillasdobles = "Hola, soy una cadena con comillas dobles"
comillastriples = '''Hola,
soy una cadena con comillas triples
'''
print(comillassimples)
print(comillasdobles)
print(comillastriples)

# numeros

a = 1 # entero
b = 2.5 # flotante
c = 1 + 2j # complejo

print(a)
print(b)
print(c)

# lista

list = ["manzana", "banana", "cereza"]  #lista es mutable
print(list)

# tupla 

tupla = ("a", "b", "c")  #tupla es inmutable
print(tupla)

#diccionario 

dict = {
    "nombre": "Juan", 
    "edad": 30, 
    "ciudad": "Nueva York"
}  #diccionario es una colección de pares clave-valor
print(dict)

# conjuntos (sets)

conjunto = {1, 2, 3, 3, 5} # los conjuntos no permiten elementos duplicados output: {1, 2, 3, 5}
print(conjunto)

#booleanos = True o False

booleano1 = True
booleano2 = False

print(booleano1)
print(booleano2)