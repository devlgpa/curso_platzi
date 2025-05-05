numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:                        #para cada valor en este caso i dentro de numeros ejecutara el codigo dentro del for
    print ("Aqui i es igual a: ", i + 1)

for i in range(3, 10):         #range genera un rango de numeros desde donde se especifique en este caso del 3 al 10
    print (i)

frutas = ["Manzana", "Pera", "Uva", "Naranja", "Tomate"]

for f in frutas:
    print (f)
    if f == "Naranja":
        print ("Naranja encontrada")

x = 0

while x < 5:           #while significa mientras asi que mientras se cumpla lacondicion se ejecutara asta que no cumpla
    
    if x ==3:
        break
    
    print (x)
    x += 1 

numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:                            
    if i == 3:                             #este if hace que al momento de que sea 3 ejecuta lo que este adentro por lo que al 3 no lo imprime
        continue                          #el continue hace que el for continue pero no imprima el 3 ya que al momento de ser 3 solo continua
    print ("Aqui i es igual a: ", i)