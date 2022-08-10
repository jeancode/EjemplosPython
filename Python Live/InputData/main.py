
#incluir la libreria serial
import serial
import time

#definir la variable serie
serie = serial.Serial('COM6', 115200)

#definir la funcion para enviar datos
def enviar_datos(datos):
    serie.write(datos.encode())
    time.sleep(0.1)
    serie.flush()   


#definir la funcion para recibir datos
def recibir_datos():
    datos = serie.readline().decode('ascii')
    return datos


while(1):

    datos = recibir_datos()
    print(datos)
    time.sleep(1)
