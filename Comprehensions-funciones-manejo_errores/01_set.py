
set_countries = {"col", "mex", "bol", "per"}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

set_types = {1, "hola", False, 12.12}
print(set_types)

#conjunto apartir de un string
set_from_string = set("hoola")
print(set_from_string)

set_from_tuples = set(("abc", "cbv", "as", "abc"))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4]
#imprime un conjunto de pero sin repetir solo unicos con "set"
set_numbers = set(numbers)
print(set_numbers)

#imprime los numeros unicos del conjunto en forma de lista
unique_numbers = list(set_numbers)
print(unique_numbers)