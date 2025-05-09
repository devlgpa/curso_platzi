
import os

#Current Working Directory
#obtener el directorio actual
"""cwd = os.getcwd()
print("directorio de trabajo actual", cwd)"""

#listar los archivos .txt
txt_files = [f for f in os.listdir(".") if f.endswith(".txt")] 
#el punto en list dir le dice que busque en el directorio actual
print ("Archivos txt: ", txt_files)

#renombrar archivo
os.rename("caperucita.txt", "cuento.txt")
print("Archivo renombrado")

#listar los archivos .txt
txt_files = [f for f in os.listdir(".") if f.endswith(".txt")] 
print ("Archivos txt: ", txt_files)

