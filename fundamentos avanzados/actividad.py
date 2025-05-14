
empleados:list = []

def add_empleados(nombre: str, edad: int, salario: float) -> dict:
        global empleados
        empleado = {
                "nombre": nombre,
                "edad": edad,
                "salario": salario
        }
        empleados.append(empleado)

def salario_mayor_a() -> list:
        resultado = []
        for empleado in empleados:
            if empleado["salario"] > 2000:
                resultado.append((empleado["nombre"], empleado["edad"]))
        return resultado

employee1 = add_empleados("Carlos", 32, 3200.0)
employee2 = add_empleados("Minerva", 25, 1900.0)
employee3 = add_empleados("Cris", 23, 1500.0)
employee4 = add_empleados("Niquita", 35, 3900.0)
employee5 = add_empleados("Gaspar", 39, 4200.0)
        
# Mostrar todos los empleados, uno por línea
print("Todos los empleados:")
for empleado in empleados:
    print(f"Nombre: {empleado['nombre']}, Edad: {empleado['edad']}, Salario: {empleado['salario']}")

# Mostrar empleados con salario mayor a 2000
print("\nEmpleados con salario mayor a 2000:")  #el \n genera un salto de linea antes del texto
for nombre, edad in salario_mayor_a():
    print(f"Nombre: {nombre}, Edad: {edad}")