
from collections import deque

def manage_delivery_queue():
    # Crea una cola para gestionar la entrega de productos
    delivery_queue = deque(['orden1', 'orden2', 'orden3'])
    delivery_queue.append('orden4')  # Añadir al final
    delivery_queue.appendleft('orden0')  # Añadir al inicio
    print(delivery_queue)  # Output: deque(['orden0', 'orden1', 'orden2', 'orden3', 'orden4'])
    delivery_queue.pop()  # Eliminar del final
    delivery_queue.popleft()  # Eliminar del inicio
    print(delivery_queue)  # Output: deque(['orden1', 'orden2', 'orden3'])

manage_delivery_queue()