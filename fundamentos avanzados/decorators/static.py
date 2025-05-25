
class Calculadora:
    #este decorador de usa cuando no necesitas acceder a una clase o modificar sus datos
    @staticmethod  
    def suma(a: int, b: int) -> int:
        return a + b