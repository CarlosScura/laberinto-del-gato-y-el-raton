# importamos las librerias necesarias
import random

# creamos las variables que necesitamos inicialmente.
laberinto = []
tamano = 5

pos_cat = (0,0) # esquina superior izuqierda
pos_rat = (0,4) # esquina superior derecha



# generamos el laberinto con el tamaño de la variable tamano.

for i in range(tamano):
    fila=[]
    for j in range(tamano):
        fila.append(' ')
        laberinto.append(fila)

def mostrar_lab():
    global laberinto
    for i in range(tamano):
        print(laberinto[i])

mostrar_lab()
