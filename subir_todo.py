import os
from datetime import datetime

# Agregar todos los archivos
os.system('git add .')

# Crear mensaje de commit con la fecha actual
fecha = datetime.now().strftime('%Y-%m-%d')
os.system(f'git commit -m "Auto-commit {fecha}"')

# Subir los cambios al repositorio remoto
os.system('git push')