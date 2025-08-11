import random
countries = ['col', 'mex', 'bol', 'pe']

population_v2 = { country: random.randint(1, 100)  for country in countries}
print(population_v2)

result = { country: population for (country, population) in population_v2.items() if population > 50 }
print(result)

text = 'Hola, soy Nicolas'
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique)

#Reto practica

def run():
    text = "Hola a todos, esta es una cadena de texto de prueba para contar."
    print(text)
    unique = { c: text.count(c) for c in text if c in 'aeiou' }
    print(f"unique: {unique}")

if __name__ == '__main__':
    run()