"""Snake, classic arcade game.

Equipo 2:
    Angel Gabriel Arce Martinez
    Elisheba Hannai Trejo Leyva

Modificaciones
1. La comida podrá moverse al azar un paso a la vez y no deberá de salirse de la ventana
2. Cada vez que se corra el juego, la víbora y la comida deberán tener colores diferentes
   entre sí, pero al azar, de una serie de 5 diferentes colores, excepto el rojo.
"""
import random
import turtle
from random import randrange, choice
from turtle import *

from freegames import square, vector

colores_s = ['blue', 'green', 'orange', 'purple', 'yellow']
colores_f = ['lightblue', 'lime', 'pink', 'cyan', 'black']

snake_color = random.choice(colores_s)
food_color = random.choice(colores_f)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def distance(pos1, pos2):
    """Calculate distance between two positions."""
    return ((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2) ** 0.5


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    # Comprobación si la cabeza está cerca de la comida. Modificada.
    if distance(head, food) < 10:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()

    move_food()  # Llame a move_food() al final de move() para actualizar la posición de los alimentos
    ontimer(move, 100)


def move_food():
    """Move food randomly."""
    directions = [vector(15, 0), vector(-10, 0), vector(0, 15), vector(0, -10)]
    direction = choice(directions)  # Elige una dirección aleatoria
    new_food_pos = food.copy()  # Hacer una copia de la posición actual de los alimentos.
    new_food_pos.move(direction)  # Mueve la comida en la dirección elegida.

    if inside(new_food_pos):  # Compruebe si la nueva posición está dentro de los límites.
        food.move(direction)  # Si es así, mueva la comida.


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
move_food()  # Iniciar el movimiento de alimentos.
done()