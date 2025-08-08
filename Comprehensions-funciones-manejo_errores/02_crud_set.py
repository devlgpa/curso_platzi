
set_countries = {"col", "mex", "bol"}

size = len(set_countries)
print(size)

print("col" in set_countries)
print("pe" in set_countries)

# add: añade un elemento unico
set_countries.add("pe")
print(set_countries)
set_countries.add("pe")
print(set_countries)

# update: añade multiples elementos
set_countries.update({"ar", "ecua", "pe"})
print(set_countries)

# remove: elimina un elemento

set_countries.remove("col")
print(set_countries)

#si remove no encuentra nada lanza error
set_countries.remove("ar")

#remueve pero si no encuentra nada no lanza error
set_countries.discard("arg")
print(set_countries)
set_countries.add("arg")
print(set_countries)

#clear: eliminia todo el conjunto
set_countries.clear()

#imprimira un set vacio
print(set_countries)
print(len(set_countries))