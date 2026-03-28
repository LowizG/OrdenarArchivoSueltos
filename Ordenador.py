import os
import shutil

#Directorio a trabajar
data = '/home/user/Downloads/'
#lista con los archivos del directorio
archivos = os.listdir(data)

# funcion para iterar en los archivos y crear un array con todas la extenciones disponibles
def iterar_Archivos(archivos):
	formatos = []
	for archivo in archivos:
		nombre, ext = os.path.splitext(archivo)
		if ext[1:] not in formatos:
			formatos.append(ext[1:])
	return formatos

def crear_Carpetas(nombres):
	for nombre in nombres:
		final = os.path.join(data, nombre)
		if not os.path.exists(final):
			os.mkdir(final)
				
def mover_Archivos(archivos):
	try:
		for archivo in archivos:
			#Separar el nombre y extencion para despues tener la direccion de la carpeta 
			# y lo quie deberia ser el directiorio con el archivo
			nombre, ext =  os.path.splitext(archivo)
			carpeta = os.path.join(data, ext[1:])
			dir_Final = os.path.join(carpeta, archivo)
			#Verificamos si existe el archivo en la carpeta, caso negativo, se mueve
			if not os.path.exists(dir_Final):
				dir_archivo = os.path.join(data, archivo)
				print(f'{archivo} moviendo a -------------------------> {carpeta}')
				shutil.move(dir_archivo, carpeta)
			else:
				print(f'{archivo} ya existente en {carpeta}')

	except IOError:
		print('Ocurrio un error leyendo', archivo)
	
lista_formatos  = iterar_Archivos(archivos)
crear_Carpetas(lista_formatos)
mover_Archivos(archivos)

