
class Circulo:

    def __init__(self, radio: float):
        self._radio = radio
    #property convierte el metodo en un atributo 
    @property
    def area(self) -> float:
        return 3.1416 * self._radio ** 2
    
    @property
    def radio(self) -> float:
        return self._radio

    #setter para modificar el valor 
    @radio.setter
    def radio(self, valor: float):
        if valor < 0:
            raise ValueError("El radio no puede ser negativo")
        self._radio = valor

circulo = Circulo(5)
print(circulo.area)
circulo.radio = -10
print(circulo.area)