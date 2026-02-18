'''
def imprimir_tablero(state):
    crear matriz 4x4 con "."
    colocar "M" en posición del ratón
    colocar "C" en posición del gato
    mostrar en consola

def movimientos_validos(state, player):
    devolver lista de posiciones dentro del tablero (no salir de 4x4)

def aplicar_movimiento(state, move, player):
    devolver nuevo estado con jugador movido

def es_terminal(state):
    True si gato == ratón (captura)
    False en otro caso

def evaluar(state):
    devolver distancia Manhattan entre gato y ratón
    (ratón quiere maximizar, gato quiere minimizar)

'''
# creamos las variables que necesitamos inicialmente.
laberinto = []

pos_cat = (0,0) # esquina superior izquierda
pos_rat = (0,4) # esquina superior derecha

tablero = {
    "cat": (0, 0),
    "mouse": (0, 4),
    "tamaño": (5, 5),
    "laberinto": [[" " for j in range(tamaño[1])] for i in range(tamaño[0])]
}

def crear_laberinto():
    global laberinto, tamano
    for i in range(tamano[0]):
        fila=[]
        for j in range(tamano[1]):
            fila.append(' ')
            laberinto.append(fila)

def mostrar_tablero():
    global tamano
    for i in range(tamano[0]):
        print(laberinto[i])