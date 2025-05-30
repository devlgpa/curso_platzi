
import datetime

def registrar_log(employee, accion):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] Empleado: {employee} realizó la acción: {accion}\n"
    with open("employee_actions.log", "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)

def marcar_asistencia(employee):
    registrar_log(employee, "marcar_asistencia")
    print(f"{employee} ha marcado su asistencia.")

def registrar_entrada_visita(employee, visitante):
    registrar_log(employee, "registrar_entrada_visita")
    print(f"{employee} ha registrado la entrada de {visitante}.")

# Ejecución de funciones
marcar_asistencia("Carlos Pérez")
registrar_entrada_visita("Ana Gómez", "Luis Torres")
