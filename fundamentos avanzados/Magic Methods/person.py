
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona: {self.nombre}, {self.edad} años"
    
    def __repr__(self):
        return f"<Persona(nombre={self.nombre}, edad={self.edad})>"
    
    def __eq__(self, other):
        return self.nombre == other.nombre and self.edad == other.edad
    
    def __lt__(self, other):
        return self.edad < other.edad

    def __le__(self, other):
        return self.edad <= other.edad
    
    def __add__(self, other):
        return self.edad + other.edad
    
p1 = Persona("Ana", 28)
p2 = Persona("Luis", 27)
p3 = Persona("Juan", 35)
resultado = p1 + p3  # Esto devuelve 63

print(p1)
print(repr(p2))
print(p1 == p3)
print(p1 < p2)
print(p1 + p2)
print(resultado)