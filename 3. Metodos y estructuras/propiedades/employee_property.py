
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary 
    """
    property permite definir métodos que se pueden utilizar como atributos. 
    Esto es útil para encapsular el acceso a los atributos, permitiendo validaciones 
    o transformaciones al obtener o establecer el valor.
    """
    #getter este devolvera la informacion
    @property
    def salary(self):
        return self._salary

    #los atributos pueden cambiar de info con setter
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salario no puede ser negativo")
        self._salary = new_salary

    #aqui eliminaremos un atributo
    @salary.deleter
    def salary(self):
        print(f"El salario de {self.name} a sido eliminado")
        del self._salary

# Crear instancia de Employee
employee = Employee("Ana", 5000)
print(employee.salary)  

# Modificar el salario de forma controlada
employee.salary = 6000
print(employee.salary)  

# Intentar establecer un salario negativo
#employee.salary = -1000  

# Eliminar el salario
del employee.salary  