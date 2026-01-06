
"""try:
    print (0/0)  # Esto generará un error
except ZeroDivisionError as error:
    print("Se ha producido un error:", error)

try:
    assert 1 != 1, "Los valores no son iguales"
except AssertionError as error: 
    print("Se ha producido un error:", error)

try:
    age = 10
    if age < 18:
        raise Exception("No se permite menores de edad")
except Exception as error:
    print("Se ha producido un error:", error)"""

#se pueden unificar par evitar repetir codigo
try:
    print (0/0)  # Esto generará un error pero como esta unificado una vez encuentra el primer eror salta al except

    assert 1 != 1, "Los valores no son iguales"

    age = 10
    if age < 18:
        raise Exception("No se permite menores de edad")
    
except (ZeroDivisionError) as error:
    print("Se ha producido un error:", error)
except (AssertionError) as error:
    print("Se ha producido un error:", error)
except (Exception) as error:
    print("Se ha producido un error:", error)

print ("hola")
print("hola 2")