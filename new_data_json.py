
import json

file_path = "products.json"

new_product = {
    "name": "Wireless Charger",
    "price": 75,
    "quantity": 100,
    "brand": "ChargeMaster",
    "category": "Accessories",
    "entry_date": "2025-05-09"
}

#abrira el documento en modo lectura(read)
with open(file_path, mode = "r") as file:
    products = json.load(file)

#aqui agregaremos al final el nuevo producto
products.append(new_product)

#abriremos el archivo en modo escritura o write
with open(file_path, mode = "w") as file:
    json.dump(products, file, indent=4)
    #la identacion son los espacios hasta que empieza el texto para que sea mas legible
    #por ejemplo hasta que empieza name hace 4 espacios y asi con los demas