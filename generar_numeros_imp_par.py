print("Numeros impares y pares")
print ("Ingrese un numero:")

numero = int(input())                   #aqui recibire un numero que ingrese pero que solo sea numero no texto

def num_impar(limit):              #esta funcion que empezara con valor 1 funcionara con un limite
    a = 1
    while a < limit+1:            #mientras a sea menor al limite generara a y le sumara 2 se pone +1 para que tambien cuente
        yield a                                         #el valor ingresado ya que no lo contaria si no tubiera el +1
        a = a + 2

print ("Los numeros impares hasta el ", numero, " son:")

for num in num_impar(numero):
    print (num)

def num_par(limit):                       #similar al impar pero comienza con el 2 para que sea par
    a = 2
    while a < limit+1:
        yield a                         #yield generara el valor de a y lo guardar en memoria
        a = a + 2

print ("Los numeros pares hasta el ", numero, " son:")

for num in num_par(numero):
    print (num)