
import random

'''
dict = {}
for i in range(1, 5):
  dict[i] = i * 2

print(dict)

dict_v2 = { i: i * 2 for i in range(1, 5)}
print(dict_v2)

import random
countries = ["col", "mex", "bol", "pe"]
population = {}
for country in countries:
  population[country] = random.randint(1, 100)

print(population)

population_v2 = { country: random.randint(1, 100)  for country in countries}
print(population_v2)
'''
names = ["nico", "zule", "santi"]
ages = [12, 56, 98]

#unir dos listas con list y zip
print(list(zip(names, ages)))

new_dict = {n: a for (n, a) in zip(names, ages)}
print(new_dict)

#prueba practica

countries = ['Colombia', 'México', 'Bolivia', 'Perú']
population_r = {c: random.randint(1, 100) for c in countries}
print(population_r)

numeros = range(1, 11)
pares_cuadrados = {n: n**2 for n in numeros if n % 3 == 0}
print(pares_cuadrados)


