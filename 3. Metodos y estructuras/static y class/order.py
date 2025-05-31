
class CalculadoraImpuestos:

    """
    método estático es un tipo de función definida dentro de una clase 
    que no requiere acceso al estado de la instancia. Puede ser llamado
    a través de la clase, eliminando la necesidad de instanciarla, lo que ahorra recursos y simplifica el código.
    """
    @staticmethod
    def calcular_impuesto(monto, tasa_impuesto):
        return monto * tasa_impuesto / 100  

# Uso del método estático llamado atraves de la clase
resultado = CalculadoraImpuestos.calcular_impuesto(1000, 60)
print(resultado)  # Salida: 600.0