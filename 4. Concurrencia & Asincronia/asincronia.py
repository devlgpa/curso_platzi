
import asyncio

"""
    El asincronismo es clave en el desarrollo de software moderno, ya que mejora la eficiencia en el manejo de tareas. 
    A diferencia del enfoque sincrónico, donde cada tarea espera a que la anterior termine, el asincronismo permite 
    enviar varias solicitudes al servidor al mismo tiempo, logrando respuestas más rápidas y mejor rendimiento del sistema.
"""

async def process_data(data):
    print(f'Procesando {data}...')
    #Simular una operación
    await asyncio.sleep(10)
    print(f'{data} procesado.')
    return data * 2

async def main():
    print('Inicio de procesamiento')
    result = await process_data('archivo.txt')
    print(f'Resultado: {result}')

asyncio.run(main())