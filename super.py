
class Person:
    def __init__(self, name, age):
        self.name = name    # Atributo
        self.age = age      # Atributo

    def greet(self):
        print("Hello! I am a person.")

class Student(Person):
    def __init__(self, name, age, student_id):
        # El super()
        # Permite llamar métodos o acceder a atributos de la **clase padre** desde una **clase hija**
        # sin necesidad de referenciar explícitamente el nombre de la clase padre
        super().__init__(name, age)
        self.student_id = student_id    # Atributo

    def greet(self):
        super().greet()
        print(f"Hello, my student ID is {self.student_id}")

student = Student("Chalo", 20, "S123")
student.greet()