import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.color("red")
turtle.bgcolor("black")

def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2*n) - 2 * math.cos(3*n) - math.cos(4*n)
    return x, y

for i in range(1, 16):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    for n in range(0, 1000):
        x, y = corazon(n / 100)
        t.goto(x * i, y * i)

t.hideturtle()
turtle.done()



