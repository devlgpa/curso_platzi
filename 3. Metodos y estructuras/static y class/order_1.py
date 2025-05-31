

"""
A diferencia de los métodos estáticos, los class methods modifican el estado de la clase. 
Se definen utilizando el decorador @classmethod y siempre reciben el parámetro cls, que representa la propia clase. 
Pueden cambiar cosas que afectan a toda la clase, no solo a un objeto.
"""
class Pedido:
    descuento_global = 10

    @classmethod
    def actualizar_descuento(cls, nuevo_descuento):
        cls.descuento_global = nuevo_descuento

# Uso del class method cambiar valor descuento global
Pedido.actualizar_descuento(15)

#aqui consultamos el calor del producto
print(Pedido.descuento_global)  # Salida: 15