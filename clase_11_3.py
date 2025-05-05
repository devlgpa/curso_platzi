is_member = True
age = 19

if is_member:                                                                 #si miembro es True ejecuta el if
    if age >= 15:
        print ("Tienes acceso ya que eras miembro y mayor o igual a 15 años")  #si cumple la condicon de se mayor o igual a 15 lo ejecuta
    else:
        print ("No tienes acceso ya que eres miembro pero menor a 15 años")  #sino lo cumple ejecuta este
else:
    print ("No eres miembro y NO TIENES ACCESO")                   #si miembro es falso ejecuta este
