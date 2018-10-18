
import turtle

window = turtle.Screen()

boi = turtle.Turtle()

boi.speed(0)

div = 1
change = 1
for i in range(1000):
    boi.forward(2 + div)
    boi.left((180 / div) - 3 * div)
    div += 1
    if i % 50 == 0:
        div = change
    if i % 10:
        change += 1

window.exitonclick()
