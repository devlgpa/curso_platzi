
class Counter:
    count = 0

    #metodo de clase usan classmethod para acceder a cls
    @classmethod
    def increment(cls):
        cls.count +=1

Counter.increment()
Counter.increment()

#imprimimos el count de la clase counter
print (Counter.count)