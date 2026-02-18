'''
import funciones
import minimax

def main():
    inicializar tablero 4x4
    colocar ratón en posición inicial
    colocar gato en posición inicial
    turnos = 0

    mientras turnos < 6 y no terminal(state):
        imprimir tablero con posiciones
        pedir al usuario movimiento del ratón (arriba/abajo/izq/der)
        validar movimiento y actualizar estado

        # turno del gato con minimax
        valor, mejor_movimiento = minimax.minimax(state, depth=2, maximizing_player=False)
        aplicar movimiento del gato

        turnos += 1

    imprimir resultado (quién ganó o si terminó por turnos)

'''
import funciones as f
import minimax


# generamos el laberinto con el tamaño de la variable tamano.
f.crear_laberinto()

f.mostrar_tablero()

