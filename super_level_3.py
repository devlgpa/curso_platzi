
class LivingBeing:
    def __init__(self, name):
        self.name = name   # Atributo

class Person(LivingBeing):
    # Aqui agregaremos edad o age a la clase livingbeing o ser vivo que solo tenia nombre
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age      # Atributo

class Student(Person):
    # Aqui a la clase persona o person le agregaremos una id
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id     # Atributo

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and my student ID is {self.student_id}")

student = Student("Carlos", 21, "S54321")
student.introduce() 