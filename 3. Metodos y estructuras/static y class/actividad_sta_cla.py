
class Verifier:
    
    general_discount = 15
    minimal_quantity = 50


    @staticmethod
    def verify(quantity):
        if quantity >= Verifier.minimal_quantity:
            print(f"La cantidad pasa el minimo: {quantity}")
            Verifier.crate_order(quantity)
        else:
            print("no se puede crear una orden ya que la cantidad no pasa el minimo")
            print(f"Orden minima: {Verifier.minimal_quantity} pecebres")

    @staticmethod
    def crate_order(quantity):
        print(f"la orden se ha creado y debe pagar: {quantity-(quantity*(Verifier.general_discount/100))}") 

Verifier.verify(100)
Verifier.verify(49)
 