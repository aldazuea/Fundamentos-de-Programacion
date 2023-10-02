
# Crear un nuevo archivo llamado my_notes.txt y escribir notas personales en él.

file=open('my_notes.txt','r')
lineas = file.readlines()
print(file)
print(lineas)

# Abrir el archivo my_notes.txt y leer su contenido línea por línea
with open("my_notes.txt", "r") as archivo:
   # Leer cada línea del archivo
   for linea in archivo.readlines():
        # Mostrar cada línea en la consola
       print(linea)
# Cerrar el archivo my_notes.txt después de realizar las operaciones necesarias
archivo.close()