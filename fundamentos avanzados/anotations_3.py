class Employee:

    # Anotaciones para establecer el tipo de dato
    name: str
    age: int
    salary: float

    def __init__(self, name:str, age:int, salary:float): # Dentro tambien ponemos anotaciones del tipo de dato
        self.name = name
        self.age = age
        self.salary = salary

    def introduce(self) -> str:   # anotacion del tipo de resultado tipo string
        return f"Hola, me llamo {self.name}, tengo {self.age}"
    
employye1 = Employee("Carlos", 30, 3500.00)
print (employye1.introduce())