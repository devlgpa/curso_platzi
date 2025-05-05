class Vehículo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True

    def vender(self):
        if self.disponible:
            self.disponible = False
            print(f"El vehículo {self.marca} ha sido vendido.")
        else:
            print(f"El vehículo {self.marca} no está disponible.")

    def estado(self):
        return self.disponible

    def get_price(self):
        return self.precio