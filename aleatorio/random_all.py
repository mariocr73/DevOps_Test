import tempfile
from pathlib import Path
import string
import random
import os

#Funcion para rellenar archivos con caracteres aleatorios 
def rellenar(numero_caracter, nombre_archivo):
  number_of_strings = 1
  length_of_string = numero_caracter
  for x in range(number_of_strings):
    K=(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
  file=open(nombre_archivo,"w")
  print("El nombre del archivo creado es: " + nombre_archivo)
  file.write(K)   
  file.close()

#Funcion para generar el # de caracteres aleatorios  que se insertaran en los archivos

def gen_carac():
  numero_carac = random.randint(1000,5000)
  return(numero_carac)  
  
#Generar un numero aleatorio de archivos
numero_arch = random.randint(10, 20)
print("El numero de archivos creados es: " + str(numero_arch))

#crear el numero aleatorio de archivos generados con nombres aleatorios 
# se crean en el directorio definido en el contenedor
array_archivos=[]
total=0
for i in range(numero_arch):
  if i == numero_arch:
    break
  
  tf = tempfile.NamedTemporaryFile(mode='w+b', prefix='New', dir='/tmp', delete=False)
  l = tf.name
  array_archivos.append(l)
  for j in array_archivos:
    #print(j)
    caracter=gen_carac()
    print("El numero de caracteres es: " + str(caracter))
    rellenar(caracter,j)
    file_size=os.stat(j)            
    print("Size of file : ", file_size.st_size, "bytes")  

