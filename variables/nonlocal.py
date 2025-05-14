
x ="local"

def outer_function():
    x = "enclosing"
    def inner_function():
        nonlocal x    #solo modificara el que este a su nivel
        x = "modified"
        print (f"El valor en inner es: {x}")
    inner_function()
    print (f"El valor outer: {x}")

outer_function()
print(x)