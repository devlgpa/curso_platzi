
import multiprocessing

"""
    Cuando los procesos deben compartir estructuras de datos complejas (como listas o diccionarios), 
    podemos usar un Manager para crear un espacio de memoria compartido entre procesos.
"""

def agregar_valores(lista_compartida):
    for i in range(5):
        lista_compartida.append(i)

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        lista_compartida = manager.list()

        proceso1 = multiprocessing.Process(target=agregar_valores, args=(lista_compartida,))
        proceso2 = multiprocessing.Process(target=agregar_valores, args=(lista_compartida,))

        proceso1.start()
        proceso2.start()

        proceso1.join()
        proceso2.join()

        print(f"Lista compartida: {lista_compartida}")

#multiprocessing.Manager nos permite crear una lista compartida entre varios procesos, facilitando la comunicación entre ellos.