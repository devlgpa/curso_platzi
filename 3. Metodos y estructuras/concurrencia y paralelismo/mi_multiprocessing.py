
import multiprocessing

"""
    A diferencia de los hilos, los procesos no comparten memoria de forma predeterminada.
    Para que dos procesos puedan compartir datos, Python proporciona 
    herramientas como multiprocessing.Queue y multiprocessing.Value.
"""

def calcular_cuadrado(numeros, cola):
    for n in numeros:
        cola.put(n * n)

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5]
    cola = multiprocessing.Queue()

    proceso = multiprocessing.Process(target=calcular_cuadrado, args=(numeros, cola))
    proceso.start()
    proceso.join()

    # Extraer resultados de la cola
    while not cola.empty():
        print(cola.get())

"""
    Usamos Queue para que el proceso secundario pueda pasar datos de vuelta al proceso principal.
"""