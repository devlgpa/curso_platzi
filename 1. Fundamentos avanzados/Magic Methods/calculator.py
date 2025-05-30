
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b

"""
    este if solo se ejecutara si lo ejecutas directamente, 
    pero si importas este if no se ejecutara donde lo importes
"""

if __name__ == "__main__":
    # Código que queremos ejecutar de manera directa
    res1 = sumar(3, 4)
    print(f"Suma: {res1}")

    print("Estas son las operaciones:")
    
    # Ejemplo de uso con suma
    res1 = sumar(3, 4)
    print(f"Suma: {res1}")
    
    # Ejemplo de uso con división
    res2 = dividir(10, 7)
    print(f"División: {res2}")