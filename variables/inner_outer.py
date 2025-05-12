
x = "global" #variable global

#funcion externa
def outer_function():
    x = "enclosing"

    #funcion interna
    def inner_dunction():
        x = "local"  #variable local
        print (x)
    
    inner_dunction()
    print (x)
outer_function()
print (x)