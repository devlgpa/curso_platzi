
empleados = []

def add_empleados(nombre, edad, salario):
        global empleados
        empleado = {
                "nombre": nombre,
                "edad": edad,
                "salario": salario
        }
        empleados.append(empleado)

def salario_mayor_al_promedio():
        resultado = [
        empleado["nombre"]
        for empleado in empleados if empleado["salario"] >= 2800
        ]
        return resultado

add_empleados("Samuel", 34, 4000)
add_empleados("Pablo", 24, 2700)
add_empleados("Daniel", 25, 2800)
add_empleados("Martha", 32, 3500)
add_empleados("Lumian", 41, 5000)

print (f"Los empleados con un salario mayor o igual a 2800 son: {salario_mayor_al_promedio()}")