
import json
#JavaScript Object Notation

#lectura del archivo
with open("products.json", mode="r") as file:
    products = json.load(file)

#mostrar el contenido
for product in products:
    #print (product)
    print (f"product: {product["name"]}, Price: {product["price"]}")