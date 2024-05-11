"""Memory, puzzle game of number pairs.

Equipo 2:
    Elisheba Hannai Trejo Leyva
    Angel Gabriel Arce Martinez

Cambios
1. Contar y desplegar el numero de taps
2. Detectar cuando todos los cuadros se han destapado
3. Central el dígito en el cuadro
4. Como un condimento de innovación al juego, Podrías utilizar
    algo diferente a los dígitos para resolver el juego y que al
    usuario le ayude a tener mejor memoria ?
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
""" Usamos números del 0 al 31 para las letras del 1 al 9 y
del 10 al 41 para las letras a partir del 10"""
tiles = [i for i in range(32)] * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0  # Variable to count taps


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark, hidden tiles, and tap count based on tap."""
    global tap_count  # Para modificar la variable global.
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        tap_count += 1  # Incrementar el recuento de toques
        print("Number of taps:", tap_count)

        # Comprueba si todos los mosaicos están revelados.
        if all(not tile_hidden for tile_hidden in hide):
            print("All tiles revealed!")


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y )
        """Ajustar las coordenadas para centrar mejor el elemento"""
        color('black')
        num_or_letter = tiles[mark]
        if num_or_letter < 10:
            write(str(num_or_letter), align='center', font=('Arial', 30, 'normal'))
        else:
            write(chr(num_or_letter + 55), align='center', font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
