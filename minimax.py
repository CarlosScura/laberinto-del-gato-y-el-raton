# importamos las funciones y la libreria copy.
import funciones as f
import copy

def minimax(tablero, profundidad, maximizando):

    # Comprobamos si se llegó a la profundidad maxima o si el juego terminó.
    # Y evaluamos el estado del juego usando la distancia Manhattan.

    if profundidad == 0 or f.fin_juego(tablero, 0):
        return f.dist_manh(tablero), None 

    # simulamos el turno del ratón.

    if maximizando:
        mejor_valor = float("-inf")
        mejor_movimiento = None

        movimientos = f.movimientos_validos(tablero, "raton")

        for mov in movimientos:
            nuevo_tablero = copy.deepcopy(tablero) # Copia del  tablero para las simulaciones.
            f.aplicar_movimiento(nuevo_tablero, mov, "raton")

            # _ ignoramos el movimiento de los niveles internos.
            valor, _ = minimax(nuevo_tablero, profundidad - 1, False)

            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = mov

        return mejor_valor, mejor_movimiento
    
    # Realizamos los movimientos del gato.

    else:
        mejor_valor = float("inf")
        mejor_movimiento = None

        movimientos = f.movimientos_validos(tablero, "gato")

        for mov in movimientos:
            nuevo_tablero = copy.deepcopy(tablero) # Copia del  tablero para las simulaciones.
            f.aplicar_movimiento(nuevo_tablero, mov, "gato")

            valor, _ = minimax(nuevo_tablero, profundidad - 1, True)

            if valor < mejor_valor:
                mejor_valor = valor
                mejor_movimiento = mov

        return mejor_valor, mejor_movimiento