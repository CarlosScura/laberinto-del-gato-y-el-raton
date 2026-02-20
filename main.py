'''
Pseudocogigo del main.

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
import minimax as mx

# creamos la funcion main que ejecutará el juego.

def main():
    turnos = 6
    print(f"Ahora vamos a jugar un juego, hay un gato que tiene hambre y un raton que quiere vivir,\ntu mision es escapar del gato y sobrevivir por {turnos} turnos")
    print("Ratón! Ratoncito por favor SOBREVIVE AL GATITO!!")
    print("Para mover al raton debes usar w: arriba\ns: abajo\na: izquierda\nd: derecha")
    while turnos > 0 and not f.fin_juego(f.tablero, turnos):
        f.mostrar_tablero()
        mov_val = f.movimientos_validos(f.tablero,"raton")
        print(f'Tus posibles moviminetos son: {mov_val}')
        print("¿Qué harás?")

        movimientos = {
            "w": (-1, 0),
            "s": (1, 0),
            "a": (0, -1),
            "d": (0, 1)
        }

        while True:
            mov = input("Ingresa el movimiento del ratón:").lower()

            # controlamos que esté en la lista de movimientos validos.
            if mov in movimientos:
                cambio_x, cambio_y = movimientos[mov]
                x, y = f.tablero["raton"]
                nueva_pos = (x + cambio_x, y + cambio_y)
                
                if nueva_pos in mov_val:
                    f.aplicar_movimiento(f.tablero, nueva_pos, "raton")
                    break
                else:
                    print("Movimiento fuera del tablero.")
            else:
                print(f"Movimiento no válido, por favor ingresa {mov_val}.")
            
        # turno del gato.
        
        valor, mejor_movimiento = mx.minimax(f.tablero, profundidad=2, maximizando=False)

        # aplicar movimiento del gato (esto se hará dentro de la función minimax, pero lo dejamos aquí para mostrar la idea)
        
        f.aplicar_movimiento(f.tablero, mejor_movimiento, "gato")
        turnos -= 1
    
    # Termina el bucle y controlamos quien ganó.

    if f.tablero["gato"] == f.tablero["raton"]:
        print("¡El gato atrapó al ratón! ¡Ganó el gato!")
    else:
        print("¡El ratón sobrevivió!\n¡GANASTE!")

main()

