
v = True
f = False

print(v)
print(f)

print(5<3)  # output: False
print(5>3)  # output: True

print(type(v))  # output: <class 'bool'>

print(bool("hola"))
print(bool("")) # si la cadena de texto esta vacia es False

# True

print(bool("abc"))
print(bool(123))
print(bool(["manzana","pera"]))

# False

print(bool(""))
print(bool(0))
print(bool([]))
print(bool(None)) # no es vacio pero es False

x = 123.5
print(isinstance(x, int))  # output: False