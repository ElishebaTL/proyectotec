"""Cannon, hitting targets with projectiles.

Equipo 2:
    Elisheba Hannai Trejo Leyva
    Angel Gabriel Arce Martinez

Cambios:
1. La velocidad del movimiento para el proyectil y los balones sea más rápida
"""

from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

# Aumentar la velocidad del proyectil y los objetivos.
projectile_velocity = 8
target_velocity = 2.5

def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Ajuste la velocidad para un movimiento más rápido
        speed.x = (x + 200) / 25 * projectile_velocity
        speed.y = (y + 200) / 25 * projectile_velocity

def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        # Adjust target velocity
        target.x -= target_velocity
        targets.append(target)

    for target in targets:
        target.x -= target_velocity

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
