
"""
métodos y atributos protegidos llevan un guión bajo _ al inicio. 
Esto no impide directamente el acceso desde el exterior, pero señala 
a otros desarrolladores que estos elementos deberían considerarse internos de la clase.
"""

"""
métodos y atributos privados restringen el acceso exclusivamente al interior de la clase. 
se indica un método o atributo como privado utilizando un doble guión bajo (__). No es una restricción absoluta, 
pero sí complica el acceso no autorizado a estos elementos:
"""
class BaseClass:
    def __init__(self):
        #ejemplo _ atributo
        self._variable_protegida = "Valor protegido"
        self.__private_variable = "Private"
    #ejemplo metodo _
    def _metodo_protegido(self):
        print("Este es un método protegido")
    #ejemplo __ 
    def __private_method(self):
        print("Ento es un metodo privado")

    def public_method(self):
        self.__private_method()
base = BaseClass()
#print(base._variable_protegida)
#base._metodo_protegido()

#desde aqui podemos acceder al metodo privado
#base.public_method()   

#llamamos a la variable privada
print (base.__private_variable)
#con el __ restringimos la visibilidad de la variable protegida