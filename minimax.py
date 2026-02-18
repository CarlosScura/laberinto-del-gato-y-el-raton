'''
def minimax(state, depth, maximizing_player):
    si depth == 0 o es_terminal(state):
        devolver evaluar(state), None

    si maximizing_player (ratón):
        inicializar max_eval = -inf
        para cada movimiento válido del ratón:
            child = aplicar_movimiento(state, move, "mouse")
            eval, _ = minimax(child, depth-1, False)
            actualizar max_eval y mejor_movimiento
        devolver max_eval, mejor_movimiento

    si no (gato):
        inicializar min_eval = +inf
        para cada movimiento válido del gato:
            child = aplicar_movimiento(state, move, "cat")
            eval, _ = minimax(child, depth-1, True)
            actualizar min_eval y mejor_movimiento
        devolver min_eval, mejor_movimiento

'''