#incluir librerias para escrbir archivos
import os
import random    


#crear funcion que genere valor random
def generarValorRandom():
    return random.randint(1,100)


def leerArchivo(ruta):
    #leer archivo
    with open(ruta, 'r') as archivo:
        #leer cada linea del archivo
        for linea in archivo:
            #imprimir linea
            print(linea)

def escrbirArchivo(ruta,contenido):
    #escrbir archivo
    with open(ruta, 'w') as archivo:
        #escrbir contenido en el archivo
        archivo.write(contenido)


def agregarDatoArchivo(ruta,contenido):
    #escrbir archivo
    with open(ruta, 'a') as archivo:
        #escrbir contenido en el archivo
        archivo.write(contenido)



#escrbirArchivo("./nombre.txt", "JeanAntonny1")
#leerArchivo("./nombre.txt")


for i in range(100):
    
    agregarDatoArchivo("./x.csv", "Sensor:," +str(generarValorRandom()) +"," +str(generarValorRandom()) + "\n")