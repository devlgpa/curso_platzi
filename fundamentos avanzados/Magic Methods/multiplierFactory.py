
class Multiplicador:
    # new ira antes que init
    def __new__(cls, factor: int):
        print(f"Creando instancia con factor {factor}")
        instance = super(Multiplicador, cls).__new__(cls)
        return instance

    def __init__(self, factor: int):
        self.factor = factor
        print(f"Inicializando con factor {factor}")

    def __call__(self, number: int) -> int:
        return number * self.factor

# Crear una instancia del Multiplicador
multi = Multiplicador(5)

result = multi(10)

print (result)